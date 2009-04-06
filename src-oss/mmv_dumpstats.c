/*
 * Copyright (C) 2001 Silicon Graphics, Inc.  All Rights Reserved.
 */

#include <pcp/mmv_stats.h>
#include <pcp/impl.h>

int 
main (int argc, char * argv[])
{
    int fd;

    if ( argc != 2 ) {
	printf ("USAGE: %s <filename>\n", argv[0]);
	exit (1);
    }

    if ( (fd = open (argv[1], O_RDONLY)) < 0 ) {
	perror (argv[1]);
    } else {
	struct stat s;
	void * addr;

	fstat (fd, &s);
	if ( (addr = __pmMemoryMap (fd, s.st_size, 0)) != NULL ) {
	    int i;
	    mmv_stats_hdr_t * hdr = (mmv_stats_hdr_t *) addr;
	    mmv_stats_toc_t * toc = 
		(mmv_stats_toc_t *)((char *)addr + sizeof (mmv_stats_hdr_t));

	    if ( strcmp (hdr->magic, "MMV") ) {
		puts ("Not an MMV-kosher file\n");
		return 0;
	    } else {
		printf ("Version    = %d\n", hdr->version);
		printf ("Generated  = %s", ctime (&hdr->g1));
	    }
            if (hdr->version != MMV_VERSION_0) {
                printf ("version %d not supported\n", hdr->version);
                return 0;
            }

	    for ( i=0; i < hdr->tocs; i++ ) {
		if ( toc[i].typ ==  MMV_TOC_VALUES ) {
		    int j;
		    mmv_stats_value_t * vals = 
			(mmv_stats_value_t *)((char *)addr + toc[i].offset);

		    printf ("Dumping %d values ... \n", toc[i].cnt);
		    for ( j=0; j < toc[i].cnt; j++ ) {
			mmv_stats_metric_t * m = 
			    (mmv_stats_metric_t *)((char *)addr + 
						  vals[j].metric);
			mmv_stats_inst_t * indom =
			    (mmv_stats_inst_t *)((char *)addr + 
						 vals[j].instance);
			printf ("%s", m->name);

			if ( m->indom >= 0 ) {
			    printf ("[%d or \"%s\"]",
				    indom->internal, indom->external);
			} 

			switch (m->type ) {
			case MMV_ENTRY_I32:
			    printf (" = %d", vals[j].val.i32);
			    break;
			case MMV_ENTRY_U32:
			    printf (" = %u", vals[j].val.u32);
			    break;
			case MMV_ENTRY_I64:
			    printf (" = %lld", (long long)vals[j].val.i64);
			    break;
			case MMV_ENTRY_INTEGRAL: {
                            struct timeval tv;
                            long long t;
                            
                            gettimeofday (&tv, NULL);
                            t = vals[j].val.i64 +
                                vals[j].extra*(tv.tv_sec*1e6 + tv.tv_usec);
                            
			    printf (" = %lld", t);
			    break;
                        }
			case MMV_ENTRY_DISCRETE: {
			    printf (" = %lld (cumulative)", (long long)vals[j].val.i64);
			    break;
                        }
			case MMV_ENTRY_U64:
			    printf (" = %llu", (unsigned long long)vals[j].val.u64);
			    break;
			case MMV_ENTRY_FLOAT:
			    printf (" = %f", vals[j].val.f);
			    break;
			case MMV_ENTRY_DOUBLE:
			    printf (" = %lf", vals[j].val.d);
			    break;
			default:
			    printf ("Unknown type %d", m->type);
			}
			putchar ('\n');
		    }
		}
	    }
	    return 0;
	}
    }
    return 1;
}
