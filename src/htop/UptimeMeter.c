/*
htop - UptimeMeter.c
(C) 2004-2011 Hisham H. Muhammad
Released under the GNU GPL, see the COPYING file
in the source distribution for its full text.
*/

#include "UptimeMeter.h"
#include "Platform.h"
#include "CRT.h"
#include "pcp/pmapi.h"

/*{
#include "Meter.h"
}*/

int UptimeMeter_attributes[] = {
   UPTIME
};

static void UptimeMeter_setValues(Meter* this, char* buffer, int len) {
//   int totalseconds = Platform_getUptime();
	/*From this point onwards the PMAPI is used to find the number of CPUs running on the system.*/
	int sts;
	char *pmclient_init[] = {"kernel.all.uptime"};
	pmID pmidlist[1];
	pmDesc desclist[1];
	pmResult *rp;
	pmAtomValue atom;
	sts = pmLookupName(1, pmclient_init, pmidlist);
	sts = pmLookupDesc(pmidlist[0], desclist);
	sts = pmFetch(1, pmidlist, &rp);
	pmExtractValue(rp->vset[0]->valfmt, rp->vset[0]->vlist, desclist[0].type, &atom, PM_TYPE_U32);
	pmFreeResult(rp);
	int totalseconds = atom.ul;
	/*From this point onwards the regular implementation of this function continues*/
   if (totalseconds == -1) {
      snprintf(buffer, len, "(unknown)");
      return;
   }
   int seconds = totalseconds % 60;
   int minutes = (totalseconds/60) % 60;
   int hours = (totalseconds/3600) % 24;
   int days = (totalseconds/86400);
   this->values[0] = days;
   if (days > this->total) {
      this->total = days;
   }
   char daysbuf[15];
   if (days > 100) {
      sprintf(daysbuf, "%d days(!), ", days);
   } else if (days > 1) {
      sprintf(daysbuf, "%d days, ", days);
   } else if (days == 1) {
      sprintf(daysbuf, "1 day, ");
   } else {
      daysbuf[0] = '\0';
   }
   snprintf(buffer, len, "%s%02d:%02d:%02d", daysbuf, hours, minutes, seconds);
}

MeterClass UptimeMeter_class = {
   .super = {
      .extends = Class(Meter),
      .delete = Meter_delete
   },
   .setValues = UptimeMeter_setValues, 
   .defaultMode = TEXT_METERMODE,
   .total = 100.0,
   .attributes = UptimeMeter_attributes,
   .name = "Uptime",
   .uiName = "Uptime",
   .caption = "Uptime: "
};
