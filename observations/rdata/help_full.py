from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import numpy as np
import os
import sys

from observations.util import maybe_download_and_extract


def help_full(path):
  """Health Evaluation and Linkage to Primary Care

  The HELP study was a clinical trial for adult inpatients recruited from
  a detoxification unit. Patients with no primary care physician were
  randomized to receive a multidisciplinary assessment and a brief
  motivational intervention or usual care, with the goal of linking them
  to primary medical care.

  A data frame with 1472 observations on the following variables.

  -  `ID` Subject ID

  -  `TIME` Interview time point

  -  `NUM_INTERVALS` Number of 6-month intervals from previous to
     current interview

  -  `INT_TIME1` # of months from baseline to current interview

  -  `DAYS_SINCE_BL` # of days from baseline to current interview

  -  `INT_TIME2` # of months from previous to current interview

  -  `DAYS_SINCE_PREV` # of days from previous to current interview

  -  `PREV_TIME` Previous interview time

  -  `DEAD` a numeric vector

  -  `A1` Gender (1=Male, 2=Female)

  -  `A9` Years of education completed

  -  `A10` Marital Status (1=Married, 2=Remarried, 3=Widowed, 4=
     Separated, 5=Divorced, 6=Never Married

  -  `A11A` Do you currently have a living mother? (0=No, 1= Yes

  -  `A11B` Do you currently have a living father? (0=No, 1=Yes

  -  `A11C` Do you currently have siblings? (0=No, 1=Yes

  -  `A11D` Do you currently have a partner (0=No, 1=Yes)

  -  `A11E` Do you currently have children? (0=No, 1=Yes)

  -  `A12B` Hollingshead categories (1=Major profess, 2= Lesser profess,
     3=Minor profess, 4=Clerical/sales, 5=Skilled manual, 6=Semi-skilled,
     7=Unskilled, 8= Homemaker, 9=No occupation)

  -  `A13` Usual employment pattern in last 6 months (1=Full time, 2=
     Part time, 3=Student, 4=Unemployed, 5=Control envir)

  -  `A14A` Loved alone-last 6 mos (0=No, 1=Yes)

  -  `A14B` Lived w/a partner-last 6 mos (0=No, 1=Yes

  -  `A14C` Lived with parent(s)-last 6 mos (0=No, 1=Yes)

  -  `A14D` Lived w/children-last 6 mos (0=No, 1=Yes)

  -  `A14E` Lived w/other family-last 6 mos (0=No, 1=Yes

  -  `A14F` Lived w/friend(s)-last 6 mos (0=No, 1=Yes)

  -  `A14G` Lived w/other-last 6 mos (0=No, 1=Yes)

  -  `A14G_T` a factor with levels `1/2 WAY HOUSE` `3/4 HOUSE`
     `ANCHOR INN` `ARMY` `ASSOCIATES` `BOARDERS`
     `BOYFRIENDS MOM` `CORRECTIONAL FACILIT` `CRACK HOUSE`
     `DEALER` `ENTRE FAMILIA` `FENWOOD` `GAVIN HSE`
     `GIRLFRIENDS DAUGHTE` `GIRLFRIENDS SON` `GIRLFRIENDS CHILDREN`
     `GIRLFRIENDS DAUGHTER` `GROUP HOME` `HALF-WAY HOUSE`
     `HALFWAY HOUSE` `HALFWAY HOUSES` `HALFWAY HSE` `HOLDING UNIT`
     `HOME BORDER` `HOMELESS` `HOMELESS SHELTER` `IN JAIL`
     `IN PROGRAMS` `INCARCERATED` `JAIL` `JAIL HALFWAY HOUSE`
     `JAIL, SHELTER` `JAIL, STREET` `JAIL/PROGRAM` `JAIL/SHELTER`
     `JAILS` `LANDLADY` `LANDLORD` `LODGING HOUSE`
     `MERIDIAN HOUSE` `NURSING HOME` `ON THE STREET`
     `PARTNERS MOTHER` `PARTNERS CHILD` `PARTNERS CHILDREN`
     `PRDGRAMS` `PRISON` `PROGRAM` `PROGRAM MTHP`
     `PROGRAM ROOMMATES` `PROGRAM SOBER HOUSE` `PROGRAM-RESIDENTIAL`
     `PROGRAM/HALFWAY HOUS` `PROGRAM/JAIL` `PROGRAM/SHELTER`
     `PROGRAM/SHELTERS` `PROGRAMS` `PROGRAMS SUBSTANCE`
     `PROGRAMS/SHELTER` `PROGRAMS/SHELTERS` `PROGRAMS/SHELTERS/DE`
     `PROJECT SOAR` `RESIDENTIAL FACILITY` `RESIDENTIAL PROGRAM`
     `ROOMING HOUSE` `ROOMING HOUSE (RELIG` `ROOMMATE` `ROOMMATES`
     `ROOMMATES AT TRANSIT` `RYAN HOUSE` `SALVATION ARMY`
     `SHELTER` `SHELTER/HALFWAY HSE` `SHELTER/HOTEL`
     `SHELTER/PROGRAM` `SHELTERS` `SHELTERS/HOSPITALS`
     `SHELTERS/JAIL` `SHELTERS/PROGRAMS` `SHELTERS/STREETS`
     `SOBER HOUSE` `SOBER HOUSING` `SOUTH BAY JAIL` `STEPSON`
     `STREET` `STREETS` `SUBSTANCE ABUSE TREA`
     `TRANSITIONAL HOUSE` `VA SHELTER`

  -  `A15A` #nights in ovrnight shelter-last 6 mos

  -  `A15B` # nights on street-last 6 mos

  -  `A15C` #months in jail-last 6 mos

  -  `A16A` # months in ovrnight shelter-last 5 yrs

  -  `A16B` #moths on street-last 5 yrs

  -  `A16C` #months in jail-last 5 yrs

  -  `A17A` Received SSI-past 6 mos (0=No, 1=Yes)

  -  `A17B` Received SSDI-past 6 mos (0=No, 1=Yes)

  -  `A17C` Received AFDC-past 6 mos (0=No, 1=Yes)

  -  `A17D` Received EAEDC-past 6 mos (0=No, 1=Yes)

  -  `A17E` Received WIC-past 6 mos (0=No, 1=Yes)

  -  `A17F` Received unemployment benefits-past 6 mos (0=No, 1=Yes)

  -  `A17G` Received Workman's Comp-past 6 mos (0=No, 1=Yes)

  -  `A17H` Received Child Support-past 6 mos (0=No, 1=Yes)

  -  `A17I` Received other income-past 6 mos (0=No, 1=Yes)

  -  `A17I_T` a factor with levels `DISABLED VETERAN`
     `EBT (FOOD STAMPS)` `EMERGENCY FOOD STAMP` `FOOD STAMP`
     `FOOD STAMPS` `FOOD STAMPS/VETERAN` `FOOD STAMPS/VETERANS`
     `INSURANCE SETTLEMENT` `PENSION CHECK` `SECTION 8`
     `SERVICE CONNECTED DI` `SOCIAL SECURITY` `SSDI FOR SON`
     `SURVIVORS BENEFITS` `TEMPORARY DISABILITY`
     `VA BENEFITS-DISABILI` `VA COMPENSATION` `VA DISABILITY PENSIO`
     `VETERAN BENEFITS` `VETERANS SERVICES` `VETERANS AFFAIRS`

  -  `A18` Most money made in any 1 year-last 5 yrs (1=<5000,
     2=5000-10000, 3=11000-19000, 4=20000-29000, 5=30000-39000,
     6=40000-49000, 7=50000+

  -  `B1` In general, how is your health (1=Excellent, 2=Very Good,
     3=Good, 4=Fair, 5=Poor)

  -  `B2` Comp to 1 yr ago, how is your health now (1=Much better,
     2=Somewhat better, 3=About the same, 4=Somewhat worse, 5=Much worse)

  -  `B3A` Does health limit you in vigorous activity (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3B` Does your health limit you in moderate activity (1=Limited a
     lot, 2=Limited a little, 3=Not limited)

  -  `B3C` Does health limit you in lift/carry groceries (1=Limited a
     lot, 2=Limited a little, 3=Not limited)

  -  `B3D` Hlth limit you in climb sev stair flights (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3E` Health limit you in climb 1 stair flight (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3F` Health limit you in bend/kneel/stoop (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3G` Does health limit you in walking >1 mile (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3H` Hlth limit you in walking sevrl blocks (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3I` Does health limit you in walking 1 block (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B3J` Hlth limit you in bathing/dressing self (1=Limited a lot,
     2=Limited a little, 3=Not limited)

  -  `B4A` Cut down wrk/act due to phys hlth-lst 4 wks (0=No, 1=Yes)

  -  `B4B` Accomplish less due to phys hlth-lst 4 wks (0=No, 1=Yes)

  -  `B4C` Lim wrk/act type due to phys hlth-lst 4 wks (0=No, 1=Yes)

  -  `B4D` Diff perf work due to phys hlth-lst 4 wks (0=No, 1=Yes)

  -  `B5A` Cut wrk/act time due to emot prbs-lst 4 wks (0=No, 1=Yes)

  -  `B5B` Accomplish ess due to emot probs-lst 4 wks (0=No, 1=Yes)

  -  `B5C` <carefl w/wrk/act due to em prb-lst 4 wks (0=No, 1=Yes)

  -  `B6` Ext phys/em intf w/norm soc act-lst 4 wk (1-Not al all,
     2=Slightly, 3=Moderately, 4=Quite a bit, 5=Extremely)

  -  `B7` Amount of bodily pain-past 4 wks (1=None, 2=Very mild, 3=
     Mild, 4=Moderate, 5= Severe, 6= Very severe)

  -  `B8` Amt pain interf with norm work-last 4 wks (1=Not at all, 2=A
     little bit, 3=Moderately, 4=Quite a bit, 5=Extremely

  -  `B9A` Did you feel full of pep-past 4 wks (1=All of the time,
     2=Most of the time, 3 = Good bit of the time, 4=Some of the time, 5=A
     little of time, 6=None of the time)

  -  `B9B` Have you been nervous-past 4 wks (1=All of the time, 2=Most
     of the time, 3 = Good bit of the time, 4=Some of the time, 5=A little
     of time, 6=None of the time)

  -  `B9C` Felt nothing could cheer you-lst 4 wks (1=All of the time,
     2=Most of the time, 3 = Good bit of the time, 4=Some of the time, 5=A
     little of time, 6=None of the time)

  -  `B9D` Have you felt calm/peaceful-past 4 wks (1=All of the time,
     2=Most of the time, 3 = Good bit of the time, 4=Some of the time, 5=A
     little of time, 6=None of the time)

  -  `B9E` Did you have a lot of energy-past 4 wks (1=All of the time,
     2=Most of the time, 3 = Good bit of the time, 4=Some of the time, 5=A
     little of time, 6=None of the time)

  -  `B9F` Did you feel downhearted-past 4 wks (1=All of the time,
     2=Most of the time, 3 = Good bit of the time, 4=Some of the time, 5=A
     little of time, 6=None of the time)

  -  `B9G` Did you feel worn out-past 4 wks (1=All of the time, 2=Most
     of the time, 3 = Good bit of the time, 4=Some of the time, 5=A little
     of time, 6=None of the time)

  -  `B9H` Have you been a happy pers-past 4 wks (1=All of the time,
     2=Most of the time, 3 = Good bit of the time, 4=Some of the time, 5=A
     little of time, 6=None of the time)

  -  `B9I` Did you feel tired-past 4 wks (1=All of the time, 2=Most of
     the time, 3 = Good bit of the time, 4=Some of the time, 5=A little of
     time, 6=None of the time)

  -  `B10` Amyphys/em prb intf w/soc act-lst 4 wks (1All of the time,
     2=Most of the time, 3=Some of the time, 4= A lttle of time, 5= Non of
     the time)

  -  `B11A` I seem to get sick easier than oth peop (1=Definitely true,
     2=Mostly True, 3=Don't know, 4=Mostly false, 5=Definitely false)

  -  `B11B` I am as healthy as anybody I know (1=Definitely true,
     2=Mostly true, 3=Don't know, 4=Mostly false, 5=Definitely False)

  -  `B11C` I expect my health to get worse (1=Definitely true, 2=Mostly
     true, 3=Don't know, 3=Mostly false, 5=Definitely false)

  -  `B11D` My health is excellent (1=Definitely true, 2=Mostly true,
     3=Don't know, 4=Mostly false, 5=Definitely false)

  -  `C1A` Tolf by MD had seix, epil, convuls (0=No, 1=Yes)

  -  `C1B` Told by MD had asth, emphys, chr lung dis (0=No, 1=Yes)

  -  `C1C` Told by MD had MI (0=No, 1=Yes)

  -  `C1D` Told by MD had CHF (0=No, 1=Yes)

  -  `C1E` Told by MD had other heart dis (req med) (0=No, 1=Yes)

  -  `C1F` Told by MD had HBP (0=No, 1=Yes)

  -  `C1G` Told by MD had chronic liver disease (0=No, 1=Yes)

  -  `C1H` Told by MD had kidney failure (0=No, 1=Yes)

  -  `C1I` Told by MD had chronic art, osteoarth (0=No, 1=Yes)

  -  `C1J` Told by MD had peripheral neuropathy (0=No, 1=Yes)

  -  `C1K` Ever told by MD had cancer (0=No, 1=Yes)

  -  `C1L` Ever told by MD had diabetes (0=No, 1=Yes)

  -  `C1M` Ever told by MD had stroke (0=No, 1=Yes)

  -  `C2A1` Have you ever had skin infections (0=No, 1=Yes)

  -  `C2A2` Have you had skin infections-past 6 mos (0=No, 1=Yes)

  -  `C2B1` Have you ever had pneumonia (0=No, 1=Yes)

  -  `C2B2` Have you had pneumonia-past 6 mos (0=No, 1=Yes)

  -  `C2C1` Have you ever had septic arthritis (0=No, 1=Yes)

  -  `C2C2` Have you had septic arthritis-past 6 mos (0=No, 1=Yes)

  -  `C2D1` Have you ever had TB (0=No, 1=Yes)

  -  `C2D2` Have you had TB-last 6 mos (0=No, 1=Yes)

  -  `C2E1` Have you ever had endocarditis (0=No, 1=Yes)

  -  `C2E2` Have you had endocarditis-past 6 mos (0=No, 1=Yes)

  -  `C2F1` Have you ever had an ulcer (0=No, 1=Yes)

  -  `C2F2` Have you had an ulcer-past 6 mos (0=No, 1=Yes)

  -  `C2G1` Have you ever had pancreatitis (0=No, 1=Yes)

  -  `C2G2` Have you had pancreatitis-past 6 mos (0=No, 1=Yes)

  -  `C2H1` Ever had abdom pain req overnt hosp stay (0=No, 1=Yes)

  -  `C2H2` Abdom pain req ovrnt hosp stay-lst 6 mos (0=No, 1=Yes)

  -  `C2I1` Have you ever vomited blood (0=No, 1=Yes)

  -  `C2I2` Have you vomited blood-past 6 mos (0=No, 1=Yes)

  -  `C2J1` Have you ever had hepatitis (0=No, 1=Yes)

  -  `C2J2` Have you had hepatitis-past 6 mos (0=No, 1=Yes)

  -  `C2K1` Ever had blood clots in legs/lungs (0=No, 1=Yes)

  -  `C2K2` Blood clots in legs/lungs-past 6 mos (0=No, 1=Yes)

  -  `C2L1` Have you ever had osteomyelitis (0=No, 1=Yes)

  -  `C2L2` Have you had osteomyelitis-past 6 mos (0=No, 1=Yes)

  -  `C2M1` Chst pain using cocaine req ER/hosp (0=No, 1=Yes)

  -  `C2M2` Chst pain using coc req ER/hosp-lst 6 mos (0=No, 1=Yes)

  -  `C2N1` Have you ever had jaundice (0=No, 1=Yes)

  -  `C2N2` Have you had jaundice-past 6 mos (0=No, 1=Yes)

  -  `C2O1` Lower back pain > 3mos req med attn (0=No, 1=Yes)

  -  `C2O2` Lwr bck pain >3mos req med attn-last 6 mos (0=No, 1=Yes)

  -  `C2P1` Ever had seizures or convulsions (0=No, 1=Yes)

  -  `C2P2` Had seizures or convulsions-past 6 mos (0=No, 1=Yes)

  -  `C2Q1` Ever had drug/alc overdose req ER attn (0=No, 1=Yes)

  -  `C2Q2` Drug/alc overdose req ER attn (0=No, 1=Yes)

  -  `C2R1` Have you ever had a gunshot wound (0=No, 1=Yes)

  -  `C2R2` Had a gunshot wound-past 6 mos (0=No, 1=Yes)

  -  `C2S1` Have you ever had a stab wound (0=No, 1=Yes)

  -  `C2S2` Have you had a stab wound-past 6 mos (0=No, 1=Yes)

  -  `C2T1` Ever had accid/falls req med attn (0=No, 1=Yes)

  -  `C2T2` Had accid/falls req med attn-past 6 mos (0=No, 1=Yes)

  -  `C2U1` Ever had fract/disloc to bones/joints (0=No, 1=Yes)

  -  `C2U2` Fract/disloc to bones/joints-past 6 mos (0=No, 1=Yes)

  -  `C2V1` Ever had injury from traffic accident (0=No, 1=Yes)

  -  `C2V2` Had injury from traffic accid-past 6 mos (0=No, 1=Yes)

  -  `C2W1` Have you ever had a head injury (0=No, 1=Yes)

  -  `C2W2` Have you had a head injury-past 6 mos (0=No, 1=Yes)

  -  `C3A1` Have you ever had syphilis (0=No, 1=Yes)

  -  `C3A2` # times had syphilis

  -  `C3A3` Have you had syphilis in last 6 mos (0=No, 1=Yes)

  -  `C3B1` Have you ever had gonorrhea (0=No, 1=Yes)

  -  `C3B2` # times had gonorrhea

  -  `C3B3` Have you had gonorrhea in last 6 mos (0=No, 1=Yes)

  -  `C3C1` Have you ever had chlamydia (0=No, 1=Yes)

  -  `C3C2` # of times had Chlamydia

  -  `C3C3` Have you had chlamydia in last 6 mos (0=No, 1=Yes)

  -  `C3D` Have you ever had genital warts (0=No, 1=Yes)

  -  `C3E` Have you ever had genital herpes (0=No, 1=Yes)

  -  `C3F1` Have you ever had other STD's (not HIV) (0=No, 1=Yes)

  -  `C3F2` # of times had other STD's (not HIV)

  -  `C3F3` Had other STD's (not HIV)-last 6 mos (0=No, 1=Yes)

  -  `C3F_T` a factor with levels `7` `CRABS`
     `CRABS - TRICHONOMIS` `CRABS, HEP B` `DOESNT KNOW NAME`
     `HAS HAD ALL 3  ABC` `HEP B` `HEP B, TRICAMONAS` `HEP. B`
     `HEPATITIS B` `HEPATITS B` `TRICHAMONAS VAGINALA`
     `TRICHAMONIS` `TRICHOMONAS` `TRICHOMONIASIS` `TRICHOMONIS`
     `TRICHOMONIS VAGINITI` `TRICHOMORAS` `TRICHONOMIS`

  -  `C3G1` Have you ever been tested for HIV/AIDS (0=No, 1=Yes)

  -  `C3G2` # times tested for HIV/AIDS

  -  `C3G3` Have you been tested for HIV/AIDS-lst 6 mos (0=No, 1=Yes)

  -  `C3G4` What was the result of last test (1=Positive, 2=Negative,
     3=Refued, 4=Never got result, 5=Inconclusive

  -  `C3H1` Have you ever had PID (0=No, 1=Yes)

  -  `C3H2` # of times had PID

  -  `C3H3` Have you had PID in last 6 mos (0=No, 1=Yes)

  -  `C3I` Have you ever had a Pap smear (0=No, 1=Yes)

  -  `C3J` Have you had a Pap smear in last 3 years (0=No, 1=Yes)

  -  `C3K` Are you pregnant (0=No, 1=Yes)

  -  `C3K_M` How many mos pregnant

  -  `D1` $ of times hospitalized for med probs

  -  `D2` Take prescr med regularly for phys prob (0=No, 1=Yes)

  -  `D3` # days had med probs-30 days bef detox

  -  `D4` How bother by med prob-30days bef detox (0=Not at all,
     1=Slightly, 2=Moderately, 3=Considerably, 4=Extremely)

  -  `D5` How import is trtmnt for these med probs (0=Not at all,
     1=Slightly, 2= Moderately, 3= Considerably, 4= Extremely

  -  `E2A` Detox prog for alc or drug prob-lst 6 mos (0=No, 1=Yes)

  -  `E2B` # times entered a detox prog-lst 6 mos

  -  `E2C` # nights ovrnight in detox prg-lst 6 mos

  -  `E3A` Holding unit for drug/alc prob-lst 6 mos (0=No, 1=Yes)

  -  `E3B` # times in holding unity=lst 6 mos

  -  `E3C` # total nights in holding unit-lst 6 mos

  -  `E4A` In halfway hse/resid facil-lst 6 mos (0=No, 1=Yes)

  -  `E4B` # times in hlfwy hse/res facil-lst 6 mos

  -  `E4C` Ttl nites in hlfwy hse/res fac-last 6 mos

  -  `E5A` In day trtmt prg for alcohol/drug-lst 6 mos (0=No, 1=Yes)

  -  `E5B` Total # days in day trtmt prg-lst 6 mos

  -  `E6` In methadone maintenance prg-lst 6 mos (0=No, 1=Yes)

  -  `E7A` Visit outpt prg subst ab couns-lst 6 mos (0=No, 1=Yes)

  -  `E7B` # visits outpt prg subst ab couns-lst 6 mos

  -  `E8A1` Saw MD/H care wkr re alcohol/drugs-lst 6 mos (0=No, 1=Yes)

  -  `E8A2` Saw Prst/Min/Rabbi re alcohol/drugs-lst 6 mos (0=No, 1=Yes)

  -  `E8A3` Employ Asst Prg for alcohol/drug prb-lst 6 mos (0=No, 1=Yes)

  -  `E8A4` Oth source cnsl for alcohol/drug prb-lst 6 mos (0=No, 1=Yes)

  -  `E9A` AA/NA/slf-hlp for drug/alcohol/emot-lst 6 mos (0=No, 1=Yes)

  -  `E9B` How often attend AA/NA/slf-hlp-lst 6 mos (1=Daily, 2=2-3
     Times/week, 3=Weekly, 4=Every 2 weeks, 5=Once/month

  -  `E10A` have you been to med clinic-lst 6 mos (0=No, 1=Yes)

  -  `E10B1` # x visit ment hlth clin/prof-lst 6 mos

  -  `E10B2` # x visited med clin/priv MD-lst 6 mos

  -  `E10C19` Visited private MD-last 6 mos (0=No, 1=Yes)

  -  `E11A` Did you stay ovrnite/+ in hosp-lst 6 mos (0=No, 1=Yes)

  -  `E11B` # times ovrnight/+ in hosp-last 6 mos

  -  `E11C` Total # nights in hosp-last 6 mos

  -  `E12A` Visited Hosp ER for med care-past 6 mos (0=No, 1=Yes)

  -  `E12B` # times visited hosp ER-last 6 mos

  -  `E13` Tlt # visits to MDs-lst 2 wks bef detox

  -  `E14A` Recd trtmt from acupuncturist-last 6 mos (0=No, 1=Yes)

  -  `E14B` Recd trtmt from chiropractor-last 6 mos (0=No, 1=Yes)

  -  `E14C` Trtd by hol/herb/hom med prac-lst 6 mos (0=No, 1=Yes)

  -  `E14D` Recd trtmt from spirit healer-lst 6 mos (0=No, 1=Yes)

  -  `E14E` Have you had biofeedback-last 6 mos (0=No, 1=Yes)

  -  `E14F` Have you underwent hypnosis-lst 6 mos (0=No, 1=Yes)

  -  `E14G` Received other treatment-last 6 mos (0=No, 1=Yes)

  -  `E15A` Tried to get subst ab services-lst 6 mos (0=No, 1=Yes)

  -  `E15B` Always able to get subst ab servies (0=No, 1=Yes)

  -  `E15C1` I could not pay for services (0=No, 1=Yes)

  -  `E15C2` I did not know where to go for help (0=No, 1=Yes)

  -  `E15C3` Couldn't get to services due to transp prob (0=No, 1=Yes)

  -  `E15C4` The offie/clinic hrs were inconvenient (0=No, 1=Yes)

  -  `E15C5` Didn't speak/understnd Englsh well enough (0=No, 1=Yes)

  -  `E15C6` Afraid other might find out about prob (0=No, 1=Yes)

  -  `E15C7` My substance abuse interfered (0=No, 1=Yes)

  -  `E15C8` Didn't have someone to watch my children (0=No, 1=Yes)

  -  `E15C9` I did not want to lose my job (0=No, 1=Yes)

  -  `E15C10` My insurance didn't cover services (0=No, 1=Yes)

  -  `E15C11` There were no beds available at the prog (0=No, 1=Yes)

  -  `E15C12` Other reason not get sub ab services (0=No, 1=Yes)

  -  `E16A1` I cannot pay for services (0=No, 1=Yes)

  -  `E16A2` I am not eligible for free care (0=No, 1=Yes)

  -  `E16A3` I do not know where to go (0=No, 1=Yes)

  -  `E16A4` Can't get to services due to trans prob (0=No, 1=Yes)

  -  `E16A5` a numeric vectorOffice/clinic hours are inconvenient (0=No,
     1=Yes)

  -  `E16A6` I don't speak/understnd enough English (0=No, 1=Yes)

  -  `E16A7` Afraid othrs find out about my hlth prob (0=No, 1=Yes)

  -  `E16A8` My substance abuse interferes (0=No, 1=Yes)

  -  `E16A9` I don't have someone to watch my childrn (0=No, 1=Yes)

  -  `E16A10` I do not want to lose my job (0=No, 1=Yes)

  -  `E16A11` My insurance doesn't cover charges (0=No, 1=Yes)

  -  `E16A12` I do not feel I need a regular MD (0=No, 1=Yes)

  -  `E16A13` Other reasons don't have regular MD (0=No, 1=Yes)

  -  `E18A` I could not pay for services (0=No, 1=Yes)

  -  `E18B` I did not know where to go for help (0=No, 1=Yes)

  -  `E18C` Couldn't get to services due to transp prob (0=No, 1=Yes)

  -  `E18D` The office/clinic hrs were inconvenient (0=No, 1=Yes)

  -  `E18F` Afraid others might find out about prob (0=No, 1=Yes)

  -  `E18G` My substance abuse interfered (0=No, 1=Yes)

  -  `E18H` Didn't have someone to watch my children (0=No, 1=Yes)

  -  `E18I` I did not want to lose my job (0=No, 1=Yes)

  -  `E18J` My insurance didn't cover services (0=No, 1=Yes)

  -  `E18K` There were no beds available at the prog (0=No, 1=Yes)

  -  `E18L` I do not need substance abuse services (0=No, 1=Yes)

  -  `E18M` Other reason not get sub ab services (0=No, 1=Yes)

  -  `F1A` Bothered by thngs not gen boethered by (0=Rarely/never,
     1=Some of the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1B` My appretite was poor (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1C` Couldn't shake blues evn w/fam+frnds hlp (0=Rarely/never,
     1=Some of the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1D` Felt I was just as good as other people (0=Rarely/never,
     1=Some of the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1E` Had trouble keeping mind on what doing (0=Rarely/never,
     1=Some of the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1F` I felt depressed (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1G` I felt everthing I did was an effort (0=Rarely/never, 1=Some
     of the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1H` I felt hopeful about the future (0=Rarely/never, 1=Some of
     the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1I` I thought my life had been a failure (0=Rarely/never, 1=Some
     of the time, 2=Occas/moderately, 3=Most of the time)

  -  `F1J` I felt fearful (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1K` My sleep was restless (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1L` I was happy (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1M` I talked less than usual (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1N` I felt lonely (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1O` People were unfriendly (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1P` I enoyed life (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1Q` I had crying spells (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1R` I felt sad (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `F1S` I felt that people dislike me (0=Rarely/never, 1=Some of the
     time, 2=Occas/moderately, 3=Most of the time)

  -  `F1T` I could not get going (0=Rarely/never, 1=Some of the time,
     2=Occas/moderately, 3=Most of the time)

  -  `G1A` Diff contr viol beh for sig time per evr (0=No, 1=Yes)

  -  `G1A_30` Diff contr viol beh-sig per lst 30 days (0=No, 1=Yes)

  -  `G1B` Ever had thoughts of suicide (0=No, 1=Yes)

  -  `G1B_30` Had thoughts of suicide-lst 30 days (0=No, 1=Yes)

  -  `G1C` Attempted suicide ever (0=No, 1=Yes)

  -  `G1C_30` Attempted suicide-lst 30 days (0=No, 1=Yes)

  -  `G1D` Prescr med for pst/emot prob ever (0=No, 1=Yes)

  -  `G1D_30` Prescr med for psy/emot prob-lst 30 days (0=No, 1=Yes)

  -  `H1_30` # days in past 30 bef detox used alcohol

  -  `H1_LT` # yrs regularly used alcohol

  -  `H1_RT` Route of administration use alcohol (0=N/A. 1=Oral,
     2=Nasal, 3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H2_30` #days in 3- bef detox use alc to intox

  -  `H2_LT` # yrs regularly used alcohol to intox

  -  `H2_RT` Route of admin use alcohol to intox (0=N/A. 1=Oral,
     2=Nasal, 3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H3_30` # days in past 30 bef detox used heroin

  -  `H3_LT` # yrs regularly used heroin

  -  `H3_RT` Route of administration of heroin (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H4_30` # days used methadone-lst 30 bef detox

  -  `H4_LT` # yrs regularly used methadone

  -  `H4_RT` Route of administration of methadone (0=N/A. 1=Oral,
     2=Nasal, 3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H5_30` # days used opi/analg-lst 30 bef detox

  -  `H5_LT` # yrs regularly used oth opiates/analg

  -  `H5_RT` Route of admin of oth opiates/analg (0=N/A. 1=Oral,
     2=Nasal, 3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H6_30` # days in past 30 bef detox used barbit

  -  `H6_LT` # yrs regularly used barbiturates

  -  `H6_RT` Route of admin of barbiturates (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H7_30` # days used sed/hyp/trnq-lst 30 bef det

  -  `H7_LT` # yrs regularly used sed/hyp/trnq

  -  `H7_RT` Route of admin of sed/hyp/trnq (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H8_30` # days in lst 30 bef detox used cocaine

  -  `H8_LT` # yrs regularly used cocaine

  -  `H8_RT` Route of admin of cocaine (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H9_30` # days in lst 30 bef detox used amphet

  -  `H9_LT` # yrs regularly used amphetamines

  -  `H9_RT` Route of admin of amphetamines (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H10_30` # days in lst 30 bef detox used cannabis

  -  `H10_LT` # yrs regularly used cannabis

  -  `H10_RT` Route of admin of cannabis (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H11_30` # days in lst 30 bef detox used halluc

  -  `H11_LT` # yrs regularly used hallucinogens

  -  `H11_RT` Route of admin of hallucinogens (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H12_30` # days in lst 30 bef detox used inhalant

  -  `H12_LT` # yrs regularly used inhalants

  -  `H12_RT` Route of admin of inhalants (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H13_30` # days used >1 sub/day-lst 30 bef detox

  -  `H13_LT` # yrs regularly used >1 subst/day

  -  `H13_RT` Route of admin of >1 subst/day (0=N/A. 1=Oral, 2=Nasal,
     3=Smoking, 4=Non-IV injection, 5=IV)

  -  `H14` Accord to interview w/c subst is main prob (0=No problem,
     1=Alcohol, 2=Alcool to intox, 3=Heroin 4=Methadone, 5=Oth
     opiate/analg, 6=Barbituates, 7=Sed/hyp/tranq, 8=Cocaine,
     9=Amphetamines, 10=Marij/cannabis

  -  `H15A` # times had alchol DTs

  -  `H15B` # times overdosed on drugs

  -  `H16A` $ spent on alc-lst 30 days bef detox

  -  `H16B` $ spent on drugs-lst 30 days bef detox

  -  `H17A` # days had alc prob-lst 30 days bef det

  -  `H17B` # days had drug prob-lst 30 days bef det

  -  `H18A` How troubled by alc probs-lst 30 days (0=Not at all,
     1=Slightly, 2=Moderately, 3=Considerably, 4=Extremely)

  -  `H18B` How troubled by drug probs-lst 30 days (0=Not at all,
     1=Slightly, 2=Moderately, 3=Considerably, 4=Extremely)

  -  `H19A` How import is trtmnt for alc probs now (0=Not at all,
     1=Slightly, 2=Moderately, 3=Considerably, 4=Extremely)

  -  `H19B` How importy is trtmnt for drug probs now (0=Not at all,
     1=Slightly, 2=Moderately, 3=Considerably, 4=Extremely)

  -  `I1` Avg # drinks in lst 30 days bef detox

  -  `I2` Most drank any 1 day in lst 30 bef detox

  -  `I3` On days used heroin, avg # bags used

  -  `I4` Most bgs heroin use any 1 day-30 bef det

  -  `I5` Avg $ amt of heorin used per day

  -  `I6A` On days used cocaine, avg # bags used

  -  `I6B` On days used cocaine, avg # rocks used

  -  `I7A` Mst bgs cocaine use any 1 day-30 bef det

  -  `I7B` Mst rcks cocaine use any 1 day-30 bef det

  -  `I8` Avg $ amt of cocaine used per day

  -  `J1` Evr don't stop using cocaine when should (0=No, 1=Yes)

  -  `J2` Ever tried to cut down on cocaine (0=No, 1=Yes)

  -  `J3` Does cocaine take up a lot of your time (0=No, 1=Yes)

  -  `J4` Need use > cocaine to get some feeling (0=No, 1=Yes)

  -  `J5A` Get phys sick when stop using cocaine (0=No, 1=Yes)

  -  `J5B` Ever use cocaine to prevent getting sick (0=No, 1=Yes)

  -  `J6` Ever don't stop using heroin when should (0=No, 1=Yes)

  -  `J7` Ever tried to cut down on heroin (0=No, 1=Yes)

  -  `J8` Does heroin take up a lot of your time (0=No, 1=Yes)

  -  `J9` Need use > heroin to get some feeling (0=No, 1=Yes)

  -  `J10A` Get phys sick when stop using heroin (0=No, 1=Yes)

  -  `J10B` Ever use heroin to prevent getting sick (0=No, 1=Yes)

  -  `K1` Do you currently smoke cigarettes (1=Yes-every day, 2=Yes-some
     days, 3=No-former smoker, 4=No-never>100 cigs

  -  `K2` Avg # cigarettes smoked per day

  -  `K3` Considering quitting cigs w/in next 6 mo (0=No, 1=Yes)

  -  `L1` How often drink last time drank (1=To get high/less, 2=To get
     drunk, 3=To pass out)

  -  `L2` Often have hangovrs Sun or Mon mornings (0=No, 1=Yes)

  -  `L3` Have you had the shakes when sobering (0=No, 1=Sometimes,
     2=Alm evry time drink)

  -  `L4` Do you get phys sick as reslt of drinking (0=No, 1=Sometimes,
     2=Alm evry time drink)

  -  `L5` have you had the DTs (0=No, 1=Once, 2=Several times

  -  `L6` When drink do you stumble/stagger/weave (0=No, 1=Sometimes,
     2=Often)

  -  `L7` D/t drinkng felt overly hot/sweaty (0=No, 1=Once, 2=Several
     times)

  -  `L8` As result of drinkng saw thngs not there (0=No, 1=Once,
     2=Several times)

  -  `L9` Panic because fear not have drink if need it (0=No, 1=Yes)

  -  `L10` Have had blkouts as result of drinkng (0=No, never,
     1=Sometimes, 2=Often, 3=Alm evry time drink)

  -  `L11` Do you carry bottle or keep close by (0=No, 1=Some of the
     time, 2=Most of the time)

  -  `L12` After abstin end up drink heavily again (0=No, 1=Sometimes,
     2=Almost evry time)

  -  `L13` Passed out due to drinking-lst 12 mos (0=No, 1=Once, 2=More
     than once)

  -  `L14` Had convuls following period of drinkng (0=No, 1=Once,
     2=Several times)

  -  `L15` Do you drink throughout the day (0=No, 1=Yes)

  -  `L16` Aftr drinkng heavily was thinkng unclear (0=No, 1=Yes, few
     hrs, 2=Yes,1-2 days, 3=Yes, many days)

  -  `L17` D/t drinkng felt heart beat rapidly (0=No, 1=Once, 2=Several
     times)

  -  `L18` Do you constntly think about drinkng/alc (0=No, 1=Yes)

  -  `L19` D/t drinkng heard things not there (0=No, 1=Once, 2= Several
     times)

  -  `L20` Had weird/fright sensations when drinkng (0=No, 1=Once or
     twice, 2=Often)

  -  `L21` When drinkng felt things rawl not there (0=No, 1=Once,
     2=Several times)

  -  `L22` With respect to blackouts (0=Never had one, 1=Had for <1hr,
     2=Had several hrs, 3=Had for day/+)

  -  `L23` Ever tried to cut down on drinking & failed (0=No, 1=Once,
     2=Several times)

  -  `L24` Do you gulp drinks (0=No, 1=Yes)

  -  `L25` After taking 1 or 2 drinks can you stop (0=No, 1=Yes)

  -  `M1` Had hangover/felt bad aftr using alcohol/drugs (0=No, 1=Yes)

  -  `M2` Felt bad about self because of alcohol/drug use (0=No, 1=Yes)

  -  `M3` Missed days wrk/sch because of alcohol/drug use (0=No, 1=Yes)

  -  `M4` Fam/frinds worry/compl about alcohol/drug use (0=No, 1=Yes)

  -  `M5` I have enjoyed drinking/using drugs (0=No, 1=Yes)

  -  `M6` Qual of work suffered because of alcohol/drug use (0=No,
     1=Yes)

  -  `M7` Parenting ability harmed by alcohol/drug use (0=No, 1=Yes)

  -  `M8` Trouble sleeping/nightmares aftr alcohol/drugs (0=No, 1=Yes)

  -  `M9` Driven motor veh while undr inf alcohol/drugs (0=No, 1=Yes)

  -  `M10` Using alcohol/1 drug caused > use othr drugs (0=No, 1=Yes)

  -  `M11` I have been sick/vomited aft alcohol/drug use (0=No, 1=Yes)

  -  `M12` I have been unhappy because of alcohol/drug use (0=No, 1=Yes)

  -  `M13` Lost weight/eaten poorly due to alcohol/drug use (0=No,
     1=Yes)

  -  `M14` Fail to do what expected due to alcohol/drug use (0=No,
     1=Yes)

  -  `M15` Using alcohol/drugs has helped me to relax (0=No, 1=Yes)

  -  `M16` Felt guilt/ashamed because of my alc drug use (0=No, 1=Yes)

  -  `M17` Said/done emarras thngs when on alcohol/drug (0=No, 1=Yes)

  -  `M18` Personality changed for worse on alcohol/drug (0=No, 1=Yes)

  -  `M19` Taken foolish risk when using alcohol/drugs (0=No, 1=Yes)

  -  `M20` Gotten into trouble because of alcohol/drug use (0=No, 1=Yes)

  -  `M21` Said cruel things while using alcohol/drugs (0=No, 1=Yes)

  -  `M22` Done impuls thngs regret due to alcohol/drug use (0=No,
     1=Yes)

  -  `M23` Gotten in phys fights when use alcohol/drugs (0=No, 1=Yes)

  -  `M24` My phys health was harmed by alcohol/drug use (0=No, 1=Yes)

  -  `M25` Using alcohol/drug helped me have more + outlook (0=No,
     1=Yes)

  -  `M26` I have had money probs because of my alcohol/drug use (0=No,
     1=Yes)

  -  `M27` My love relat harmed due to my alcohol/drug use (0=No, 1=Yes)

  -  `M28` Smoked tobacco more when using alcohol/drugs (0=No, 1=Yes)

  -  `M29` <y phys appearance harmed by alcohol/drug use (0=No, 1=Yes)

  -  `M30` My family hurt because of my alc drug use (0=No, 1=Yes)

  -  `M31` Close relationsp damaged due to alcohol/drug use (0=No,
     1=Yes)

  -  `M32` Spent time in jail because of my alcohol/drug use (0=No,
     1=Yes)

  -  `M33` My sex life suffered due to my alcohol/drug use (0=No, 1=Yes)

  -  `M34` Lost interst in activity due to my alcohol/drug use (0=No,
     1=Yes)

  -  `M35` Soc life> enjoyable when using alcohol/drug (0=No, 1=Yes)

  -  `M36` Spirit/moral life harmed by alcohol/drug use (0=No, 1=Yes)

  -  `M37` Not had kind life want due to alcohol/drug use (0=No, 1=Yes)

  -  `M38` My alcohol/drug use in way of personal growth (0=No, 1=Yes)

  -  `M39` My alcohol/drug use damaged soc life/reputat (0=No, 1=Yes)

  -  `M40` Spent/lost too much $ because alcohol/drug use (0=No, 1=Yes)

  -  `M41` Arrested for DUI of alc or oth drugs (0=No, 1=Yes)

  -  `M42` Arrested for offenses rel to alcohol/drug use (0=No, 1=Yes)

  -  `M43` Lost marriage/love relat due to alcohol/drug use (0=No,
     1=Yes)

  -  `M44` Susp/fired/left job/sch due to alcohol/drug use (0=No, 1=Yes)

  -  `M45` I used drugs moderately w/o having probs (0=No, 1=Yes)

  -  `M46` I have lost a friend due to my alcohol/drug use (0=No, 1=Yes)

  -  `M47` Had an accident while using alcohol/drugs (0=No, 1=Yes)

  -  `M48` Phys hurt/inj/burned when using alcohol/drugs (0=No, 1=Yes)

  -  `M49` I injured someone while using alcohol/drugs (0=No, 1=Yes)

  -  `M50` Damaged things/prop when using alcohol/drugs (0=No, 1=Yes)

  -  `N1A` My friends give me the moral support I need (0=No, 1=Yes)

  -  `N1B` Most people closer to friends than I am (0=No, 1=Yes)

  -  `N1C` My friends enjoy hearing what I think (0=No, 1=Yes)

  -  `N1D` I rely on my friends for emot support (0=No, 1=Yes)

  -  `N1E` Friend go to when down w/o feel funny later (0=No, 1=Yes)

  -  `N1F` Frnds and I open re what thnk about things (0=No, 1=Yes)

  -  `N1G` My friends sensitive to my pers needs (0=No, 1=Yes)

  -  `N1H` My friends good at helping me solve probs (0=No, 1=Yes)

  -  `N1I` have deep sharing relat w/ a # of frnds (0=No, 1=Yes)

  -  `N1J` When confide in frnds makes me uncomfort (0=No, 1=Yes)

  -  `N1K` My friends seek me out for companionship (0=No, 1=Yes)

  -  `N1L` Not have as int relat w/frnds as others (0=No, 1=Yes)

  -  `N1M` Recent good idea how to do somethng frm frnd (0=No, 1=Yes)

  -  `N1N` I wish my friends were much different (0=No, 1=Yes)

  -  `N2A` My family gives me the moral support I need (0=No, 1=Yes)

  -  `N2B` Good ideas of how do/make thngs from fam (0=No, 1=Yes)

  -  `N2C` Most peop closer to their fam than I am (0=No, 1=Yes)

  -  `N2D` When confide make close fam membs uncomf (0=No, 1=Yes)

  -  `N2E` My fam enjoys hearing about what I think (0=No, 1=Yes)

  -  `N2F` Membs of my fam share many of my intrsts (0=No, 1=Yes)

  -  `N2G` I rely on my fam for emot support (0=No, 1=Yes)

  -  `N2H` Fam memb go to when down w/o feel funny (0=No, 1=Yes)

  -  `N2I` Fam and I open about what thnk about thngs (0=No, 1=Yes)

  -  `N2J` My fam is sensitive to my personal needs (0=No, 1=Yes)

  -  `N2K` Fam memb good at helping me solve probs (0=No, 1=Yes)

  -  `N2L` Have deep sharing relat w/# of fam membs (0=No, 1=Yes)

  -  `N2M` Makes me uncomf to confide in fam membs (0=No, 1=Yes)

  -  `N2N` I wish my family were much different (0=No, 1=Yes)

  -  `O1A` # people spend tx w/who drink alc (1=None, 2= A few, 3=About
     half, 4= Most, 5=All)

  -  `O1B` # people spend tx w/who are heavy drinkrs (1=None, 2= A few,
     3=About half, 4= Most, 5=All)

  -  `O1C` # people spend tx w/who use drugs (1=None, 2= A few, 3=About
     half, 4= Most, 5=All)

  -  `O1D` # peop spend tx w/who supprt your abstin (1=None, 2= A few,
     3=About half, 4= Most, 5=All)

  -  `O2` Does live-in part/spouse drink/use drugs (0=No, 1=Yes, 2=N/A)

  -  `P1A` Phys abuse/assaul by fam memb/pers know (0=No, 1=Yes, 7=Not
     sure)

  -  `P1B` Age first phys assaulted by pers know

  -  `P1C` Phys assaulted by pers know-last 6 mos (0=No, 1=Yes)

  -  `P2A` Phys abuse/assaul by stranger (0=No, 1=Yes, 7=Not sure)

  -  `P2B` Age first phys assaulted by stranger

  -  `P2C` Phys assaulted by stranger-last 6 mos (0=No, 1=Yes)

  -  `P3` Using drugs/alc when phys assaulted (1=Don't know, 2=Never,
     3=Some cases, 4=Most cases, 5=All cases, 9=Never assaulted)

  -  `P4` Pers who phys assault you using alcohol/drugs (1=Don't know,
     2=Never, 3=Some cases, 4=Most cases, 5=All cases, 9=Never assaulted)

  -  `P5A` Sex abuse/assual by fam memb/pers know (0=No, 1= Yes, 7=Not
     sure)

  -  `P5B` Age first sex assaulted by pers know

  -  `P5C` Sex assaulted by pers know-last 6 mos (0=No, 1=Yes)

  -  `P6A` Sex abuse/assaul by stranger (0=No, 1=Yes, 7=Not sure)

  -  `P6B` Age first sex assaulted by stranger

  -  `P6C` Sex assaulted by stranger-last 6 mos (0=No, 1=Yes)

  -  `P7` Using drugs/alc when sex assaulted (1=Don't know, 2=Never,
     3=Some cases, 4=Most cases, 5=All cases, 9=Never assaulted)

  -  `P8` Person who sex assaulted you using alcohol/drugs (1=Don't
     know, 2=Never, 3=Some cases, 4=Most cases, 5=All cases, 9=Never
     assaulted)

  -  `Q1A` Have you ever injected drugs (0=No, 1=Yes)

  -  `Q1B` Have you injected drugs-lst 6 mos (0=No, 1=Yes)

  -  `Q2` Have you shared needles/works-last 6 mos (0=No/Not shot up,
     3=Yes)

  -  `Q3` # people shared needles w/past 6 mos (0=No/Not shot up, 1=1
     other person, 2=2-3 diff people, 3=4/+ diff people)

  -  `Q4` How often been to shoot gall/hse-lst 6 mos (0=Never, 1=Few
     times or less, 2= Few times/month, 3= Once or more/week)

  -  `Q5` How often been to crack house-last 6 mos (0=Never, 1=Few times
     or less, 2=Few times/month, 3=Once or more/week)

  -  `Q6` How often shared rinse-water-last 6 mos (0=Nevr/Not shot up,
     1=Few times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q7` How often shared a cooker-last 6 mos (0=Nevr/Not shot up,
     1=Few times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q8` How often shared a cotton-last 6 mos (0=Nevr/Not shot up,
     1=Few times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q9` How often use syringe to div drugs-lst 6 mos (0=Nevr/Not shot
     up, 1=Few times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q10` How would you describe yourself (0=Straight, 1=Gay/bisexual)

  -  `Q11` # men had sex w/in past 6 months (0=0 men, 1=1 man, 2=2-3
     men, 3=4+ men

  -  `Q12` # women had sex w/in past 6 months (0=0 women, 1=1woman,
     2=2-3 women, 3=4+ women

  -  `Q13` # times had sex In past 6 mos (0=Never, 1=Few times or less,
     2=Few times/month, 3=Once or more/week)

  -  `Q14` How often had sex to get drugs-last 6 mos (0=Never, 1=Few
     times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q15` How often given drugs to have sex-lst 6 mos (0=Never, 1=Few
     times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q16` How often were you paid for sex-lst 6 mos (0=Never, 1=Few
     times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q17` How often you pay pers for sex-lst 6 mos (0=Never, 1=Few
     times or less, 2=Few times/month, 3=Once or more/week)

  -  `Q18` How often use condomes during sex=lst 6 mos (0=No sex/always,
     1=Most of the time, 2=Some of the time, 3=None of the time)

  -  `Q19` Condoms are too much of a hassle to use (1=Strongly disagree,
     2=Disagree, 3= Agree, 4=Strongly agree)

  -  `Q20` Safer sex is always your responsibility (1=Strongly disagree,
     2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1A` I really want to hange my alcohol/drug use (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1B` Sometimes I wonder if I'm an alcohol/addict (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1C` Id I don't chng alcohol/drug probs will worsen (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1D` I started making changes in alcohol/drug use (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1E` Was using too much but managed to change (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1F` I wonder if my alcohol/drug use hurting othrs (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1G` I am a prob drinker or have drug prob (1=Strongly disagree,
     2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1H` Already doing thngs to chnge alcohol/drug use (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1I` have changed use-trying to not slip back (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1J` I have a serious problem w/ alcohol/drugs (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1K` I wonder if I'm in contrl of alcohol/drug use (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1L` My alcohol/drug use is causing a lot of harm (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1M` Actively curring down/stopping alcohol/drug use (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1N` Want help to not go back to alcohol/drugs (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1O` I know that I have an alcohol/drug problem (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1P` I wonder if I use alcohol/drugs too much (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1Q` I am an alcoholic or drug addict (1=Strongly disagree,
     2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1R` I am working hard to change alcohol/drug use (1=Strongly
     disagree, 2=Disagree, 3= Agree, 4=Strongly agree)

  -  `R1S` Some changes-want help from going back (1=Strongly disagree,
     2=Disagree, 3= Agree, 4=Strongly agree)

  -  `S1A` At interview pt obviously depressed/withdrawn (0=No, 1=Yes)

  -  `S1B` at interview pt obviously hostile (0=No, 1=Yes)

  -  `S1C` At interview pt obviouslt anx/nervous (0=No, 1=Yes)

  -  `S1D` Trouble w/real tst/thght dis/par at interview (0=No, 1=Yes)

  -  `S1E` At interview pt trbl w/ compr/concen/rememb (0=No, 1=Yes)

  -  `S1F` At interview pt had suicidal thoughts (0=No, 1=Yes)

  -  `T1` Have used alc since leaving River St. (0=No, 1=Yes)

  -  `T1B` # days in row continued to drink

  -  `T1C` Longest period abstain-lst 6 mos (alc)

  -  `T2` Have used heroin since leaving River St (0=No, 1=Yes)

  -  `T2B` # days in row continued to use heroin

  -  `T2C` Longest period abstain-lst 6 mos (heroin)

  -  `T3` Have used cocaine since leaving River St (0=No, 1=Yes)

  -  `T3B` # days in row continued to use cocaine

  -  `T3C` Lngest period abstain-lst 6 mos (cocaine)

  -  `U1` It is important to have a regular MD (1=Strongly agree,
     2=Agree, 3=Uncertain, 4=Disagree, 5=Strongly Disagree)

  -  `U2A` I cannot pay for services (0=No, 1=Yes)

  -  `U2B` I am not eligible for free care (0=No, 1=Yes)

  -  `U2C` I do not know where to go (0=No, 1=Yes)

  -  `U2D` Can't get services due to transport probs (0=No, 1=Yes)

  -  `U2E` Office/clinic hours are inconvenient (0=No, 1=Yes)

  -  `U2F` I do not speak/understand English well (0=No, 1=Yes)

  -  `U2G` Afraid others discover hlth prb I have (0=No, 1=Yes)

  -  `U2H` My substance abuse interferes (0=No, 1=Yes)

  -  `U2I` I do not have a babysitter (0=No, 1=Yes)

  -  `U2J` I do not want to lose my job (0=No, 1=Yes)

  -  `U2K` My insurance does not cover services (0=No, 1=Yes)

  -  `U2L` Medical care is not important to me (0=No, 1=Yes)

  -  `U2M` I do not have time (0=No, 1=Yes)

  -  `U2N` Med staff do not treat me with respect (0=No, 1=Yes)

  -  `U2O` I do not trust my doctors or nurses (0=No, 1=Yes)

  -  `U2P` Often been unsatisfied w/my med care (0=No, 1=Yes)

  -  `U2Q` Other reason hard to get regular med care (0=No, 1=Yes)

  -  `U2Q_T` a factor with many levels

  -  `U2R` a factor with levels `7` `A` `B` `C` `D` `E`
     `F` `G` `H` `I` `J` `K` `L` `M` `N` `O` `P`
     `Q`

  -  `U3A` Has MD evr talked to you about drug use (0=No, 1=Yes)

  -  `U3B` Has MD evr talked to you about alc use (0=No, 1=Yes)

  -  `U4` Is there an MD you consider your regular MD (0=No, 1=Yes)

  -  `U5` Have you seen any MDs in last 6 mos (0=No, 1=Yes)

  -  `U6A` Would you go to this MD if med prb not emer (0=No, 1=Yes)

  -  `U6B` Think one of these could be your regular MD (0=No, 1=Yes)

  -  `PCP_ID` a numeric vector

  -  `U7A` What type of MD is your regular MD/this MD (1=OB/GYN,
     2=Family medicine, 3=Pediatrician, 4=Adolescent medicine, 5=Internal
     medicine, 6=AIDS doctor, 7=Asthma doctor, 8=Pulmonary doctor,
     9=Cardiologist, 10=Gastroen)

  -  `U7A_T` a factor with levels `ARTHRITIS DOCTOR` `CHIROPRACTOR`
     `COCAINE STUDY` `DETOX DOCTOR` `DO` `EAR DOCTOR`
     `EAR SPECIALIST` `EAR, NOSE, & THROAT.` `EAR/NOSE/THROAT`
     `ENT` `FAMILY PHYSICIAN` `GENERAL MEDICINE`
     `GENERAL PRACTICE` `GENERAL PRACTIONER` `GENERAL PRACTITIONER`
     `HEAD & NECK SPECIALIST` `HERBAL/HOMEOPATHIC/ACUPUNCTURE`
     `ID DOCTOR` `MAYBE GENERAL PRACTITIONER` `MEDICAL STUDENT`
     `NEUROLOGIST` `NURSE` `NURSE PRACTICIONER`
     `NURSE PRACTITIONER` `ONCOLOGIST` `PRENATAL` `PRIMARY`
     `PRIMARY CAAE` `PRIMARY CARE` `PRIMARY CARE DOCTOR`
     `PRIMERY CARE` `THERAPIST` `UROLOGIST` `WOMENS CLINIC BMC`

  -  `U8A` Only saw this person once (=Only saw once)

  -  `U8B` Saw this person for <6 mos (1=<6 mos)

  -  `U8C` Saw tis person for 6 mos-1year (2=Betwn 6 mos & 1 yr)

  -  `U8D` Saw this person for 1-2 years (3=1-2 years)

  -  `U8E` Saw this person for 3-5 years (4=3-5 years)

  -  `U8F` Saw this person for more than 5 years (5=>5 years)

  -  `U10A` # times been to regular MDs office-pst 6 mos

  -  `U10B` # times saw regular MD in office-pst 6 mos

  -  `U10C` # times saw oth prof in office-pst 6 mos

  -  `U11` Rate convenience of MD office location (1=Very poor, 2=Poor,
     3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U12` Rate hours MD office open for med appts (1=Very poor, 2=Poor,
     3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U13` Usual wait for appt when sick (unsched) (1=Very poor, 2=Poor,
     3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U14` Time wait for appt to start at MD office (1=Very poor,
     2=Poor, 3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U15A` DO you pay for any/all of MD visits (0=No, 1=Yes)

  -  `U15B` How rate amt of $ you pay for MD visits (1=Very poor,
     2=Poor, 3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U16A` Do you pay for any/all of prescript meds (0=No, 1=Yes)

  -  `U16B` Rate amt $ pay for meds/prescript trtmnts (1=Very poor,
     2=Poor, 3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U17` Ever skip meds/trtmnts because too expensive (1=Yes, often,
     2=Yes, occasionally, 3=No, never)

  -  `U18A` Ability to reach MC office by phone (1=Very poor, 2=Poor,
     3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U18B` Ability to speak to MD by phone if need (1=Very poor,
     2=Poor, 3=Fair, 4=Good, 5=Very good, 6=Excellent)

  -  `U19` How often see regular MD when have regular check-up
     (1=Always, 2=Almost always, 3=A lot of the time, 4=Some of the time,
     5=Almost never, 6=Never)

  -  `U20` When sick + go to MD how often see regular MD (1=Always,
     2=Almost always, 3=A lot of the time, 4=Some of the time, 5=Almost
     never, 6=Never)

  -  `U21A` How thorough MD exam to check hlth prb (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U21B` How often question if MD diagnosis right (1=Always, 2=Almost
     always, 3=A lot of the time, 4=Some of the time, 5=Almost never,
     6=Never)

  -  `U22A` Thoroughness of MD questions re symptoms (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U22B` Attn MD gives to what you have to say (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U22C` MD explanations of hlth prbs/trtmnts need (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U22D` MD instrcts re sympt report/further care (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U22E` MD advice in decisions about your care (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U23` How often leave MD office w/unanswd quests (1=Always,
     2=Almost always, 3=A lot of the time, 4=Some of the time, 5=Almost
     never, 6=Never)

  -  `U24A` Amount of time your MD spends w/you (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U24B` MDs patience w/ your questions/worries (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U24C` MDs friendliness and warmth toward you (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U24D` MDs caring and concern for you (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U24E` MDs respect for you (1=Very poor, 2= Poor, 3=Fair, 4=Good,
     5= Very good, 6= Excellent)

  -  `U25A` Reg MD ever talked to you about smoking (0=No, 1=Yes)

  -  `U25B` Reg MD ever talked to you about alc use (0=No, 1=Yes)

  -  `U25C` Reg MD ever talk to you about seat belt use (0=No, 1=Yes)

  -  `U25D` Reg MD ever talked to you about diet (0=No, 1=Yes)

  -  `U25E` Reg Mdever talked to you about exercise (0=No, 1=Yes)

  -  `U25F` Reg MD ever talked to you about stress (0=No, 1=Yes)

  -  `U25G` Reg MD ever talked to you about safe sex (0=No, 1=Yes)

  -  `U25H` Reg MD ever talked to you about drug use (0=No, 1=Yes)

  -  `U25I` Reg MD ever talked to you about HIV testing (0=No, 1=Yes)

  -  `U26A` Cut/quit smoking because of MDs advice (0=No, 1=Yes)

  -  `U26B` Tried to drink less alcohol because of MD advice (0=No,
     1=Yes)

  -  `U26C` Wore my seat belt more because of MDs advice (0=No, 1=Yes)

  -  `U26D` Changed diet because of MDs advice (0=No, 1=Yes)

  -  `U26E` Done more exercise because MDs advice (0=No, 1=Yes)

  -  `U26F` Relax/reduce stress because of MDs advice (0=No, 1=Yes)

  -  `U26G` Practiced safer sex because of MDs advice (0=No, 1=Yes)

  -  `U26H` Tried to cut down/quit drugs because MD advice (0=No,
     1=Yes)"

  -  `U26I` Got HIV tested because of MDs advice (0=No, 1=Yes)"

  -  `U27A` I can tell my MD anything (1=Strongly agree, 2= Agree, 3=
     Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U27B` My MD pretends to know thngs if not sure (1=Strongly agree,
     2= Agree, 3= Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U27C` I trust my MDs judgement re my med care (1=Strongly agree,
     2= Agree, 3= Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U27D` My MD cares > about < costs than my hlth (1=Strongly agree,
     2= Agree, 3= Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U27E` My MD always tell truth about my health (1=Strongly agree,
     2= Agree, 3= Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U27F` My MD cares as much as I about my hlth (1=Strongly agree, 2=
     Agree, 3= Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U27G` My MD would try to hide a mistake in trtmt (1=Strongly
     agree, 2= Agree, 3= Not sure, 4=Disagree, 5=Strongly disagree)"

  -  `U28` How much to you trst this MD (0=Not at all, 1=1, 2=2, 3=3,
     4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=Completely)"

  -  `U29A` MDs knowledge of your entire med history (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)"

  -  `U29B` MD knowldg of your respons-home/work/sch (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)"

  -  `U29C` MD knowldg of what worries you most-hlth (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)"

  -  `U29D` MDs knowledge of you as a person (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)"

  -  `U30` MD would know what want done if unconsc (1=Strongly agree,
     2=Agree, 3=Not sure, 4= Disagree, 5=Strongly disagree)"

  -  `U31` Oth MDs/RNs who play roel in your care (0=No, 1=Yes)" \*

  -  `U32A` Their knowledge of you as a person (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U32B` The quality of care they provide (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U32C` Coordination betw them and your regular MD (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U32D` Their expl of your hlth prbs/trtmts need (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U32D_T` N/A, only my regular MD does this

  -  `U33` Amt regular MD knows about care from others (1=Knows
     everything, 2=Knows almost everything, 3=Knows some things, 4=Knows
     very little, 5=Knows nothing)

  -  `U34` Has MD ever recommended you see MD sepcialist (0=No, 1=Yes)

  -  `U35A` How helpful MD in deciding on specialist (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U35B` How helpful MD getting appt w/specialist (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U35C` MDs involvmt when you trtd by specialist (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U35D` MDs communic w/your specialists/oth MDs (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U35E` MD help in explain what specialists said (1=Very poor, 2=
     Poor, 3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U35F` Quality of specialists MD sent you to (1=Very poor, 2= Poor,
     3=Fair, 4=Good, 5= Very good, 6= Excellent)

  -  `U36` How many minutes to get to MDs office (1=<15, 2=16-30.
     3=31-60, 4=More than 60)

  -  `U37` When sick+call how long take to see you (1=Same day, 2=Next
     day, 3=In 2-3 days, 4=In 4-5 days, 5=in >5 days)

  -  `U38` How mant minutes late appt usually begin (1=None, 2=<5
     minutes, 3=6-10 minutes, 4=11-20 minutes, 5=21-30 minutes, 6=31-45
     minutes, 7=>45 minutes)

  -  `U39` How satisfied are you w/your regular MD (1=Completely
     satisfied, 2=Very satisfied, 3=Somewhat satisfied, 4=Neither,
     5=Somewhat dissatisfied, 6=Very dissatisfied, 7=Completely
     dissatisfied)

  -  `V1` Evr needed to drink much more to get effect (0=No, 1=Yes)

  -  `V2` Evr find alc had < effect than once did (0=No, 1=Yes)

  -  `Z1` Breath Alcohol Concentration:1st test

  -  `Z2` Breath Alcohol Concentration:2nd test

  -  `AGE` Age in years

  -  `REALM` REALM score

  -  `E16A_RT` Barrier to regular MD: red tape (0=No, 1=Yes)

  -  `E16A_IB` Barrier to regular MD: internal barriers (0=No, 1=Yes)

  -  `E16A_TM` Barrier to regular MD: time restrictions (0=No, 1=Yes)

  -  `E16A_DD` Barrier to regular MD: dislike docs/system (0=No, 1=Yes)

  -  `GROUP` Randomization Group (0=Control, 1=Clinic)

  -  `MMSEC` MMSEC

  -  `PRIM_SUB` First drug of choice (0=None, 1=Alcohol, 3=Cocaine,
     3=Heroine, 4=Barbituates, 5=Benzos, 6=Marijuana, 7=Methadone,
     8=Opiates)

  -  `SECD_SUB` Second drug of choice (0=None, 1=Alcohol, 3=Cocaine,
     3=Heroine, 4=Barbituates, 5=Benzos, 6=Marijuana, 7=Methadone,
     8=Opiates)

  -  `ALCOHOL` 1st/2nd drug of coice=Alcohol (0=No, 1=Yes)

  -  `COC_HER` 1st/2nd drug of choice=cocaine or heroine (0=No, 1=Yes)

  -  `REALM2` REALM score (dichotomous) (1=0-60, 2=61-66)

  -  `REALM3` REALM score (categorical) (1=0-44), 2=45-60), 3=61-66)

  -  `RACE` Race (recode) (1=Afr Amer/Black, 2=White, 3=Hispanic,
     4=Other)

  -  `RACE2` Race (recode) (1=White, 2=Minority)

  -  `BIRTHPLC` Where born (recode) (0=USA, 1=Foreign)

  -  `PRIMLANG` First language (recode) (0=English, 1=Other lang)

  -  `MD_LANG` Lang prefer to speak to MD (recode) (0=English, 1=Other
     lang)

  -  `HS_GRAD` High school graduate (0=No, 1=Yes)

  -  `MAR_STAT` Marital status (recode) (0=Married, 1=Not married)

  -  `A12B_REC` Hollingshead category (recode) (0=Cat 1,2,3, 1=Cat
     4,5,6, 2=Cat 7,8,9)

  -  `UNEMPLOY` Usually unemployed last 6m (0=No, 1=Yes)

  -  `ALONE6M` Usually lived alone past 6m y/n (0=No, 1=Yes)

  -  `HOMELESS` Homeless-shelter/street past 6 m (0=No, 1=Yes)

  -  `JAIL_MOS` Total months in jail past 5 years

  -  `JAIL_5YR` Any jail time past 5 years y/n (0=No, 1=Yes)

  -  `GOV_SUPP` Received governemtn support past 6 m (0=No, 1=Yes)

  -  `A18_REC1` Most money made in 1 yr (recode) (0=$19,000 or less,
     1=$20,000-$49,000, 2=$50,000 or more)

  -  `A18_REC2` Most money made-continuous recode

  -  `STD_EVER` Ever had an STD y/n (0=No, 1=Yes)

  -  `STD_6M` Had an STD past 6m y/n (0=No, 1=Yes)

  -  `CHR_SUM` Sum chronic medican conds/HIV ever

  -  `CHR_EVER` Chronic medical conds/HIV-ever y/n (0=No, 1=Yes)

  -  `EPI_SUM` Sum episodic (C2A-C2O, C2R-C2U, STD)-6m

  -  `EPI_6M` Episodic (C2A-C2O,C2R-C2U, STD)-6m y/n (0=No, 1=Yes)

  -  `EPI_6M2B` Episodic(C2A-C2O)-6m y/n (0=No, 1=Yes)

  -  `SER_INJ` Recent (6m) serious injury y/n (0=No, 1=Yes)

  -  `D3_REC` Any medical problems past 30d y/n (0=No, 1=Yes)

  -  `D4_REC` Bothered by medical problems y/n (0=No, 1=Yes)

  -  `D5_REC` Medical trtmt is important y/n (0=No, 1=Yes)

  -  `ANY_INS` Did you have health insurance past 6 m (0=No, 1=Yes)

  -  `FRML_SAT` Formal substance abuse treatment y/n (0=No, 1=Yes)

  -  `E10B1_R` Mental health treatment past 6m y/n (0=No, 1=Yes)

  -  `E10B2_R` Med clinic/private MD past 6m y/n (0=No, 1=Yes)

  -  `ALT_TRT` Alternative tratments y/n (0=No, 1=Yes)

  -  `ANY_UTIL` Amy recent health utilization (0=No, 1=Yes)

  -  `NUM_BARR` # of perceived barriers to linkage

  -  `G1B_REC` Suicidal thoughs past 30 days y/n (0=No, 1=Yes)

  -  `G1D_REC` Prescribed psych meds past 30 daus y/n (0=No, 1=Yes)

  -  `PRIMSUB2` First drug of choice (no marijuana) (0=None, 1=Alcohol,
     2=Cocaine, 3=Heroin, 4=Barbituates, 5=Benzos, 6=Marijuana,
     7=Methadone, 8=Opiates)

  -  `ALCQ_30` Total number drinks past 30 days

  -  `H2_PRB` Problem sub: alc to intox (0=No, 1=Yes)

  -  `H3_PRB` Problem sub: heroin (0=No, 1=Yes)

  -  `H4_PRB` Problem sub: methadone (0=No, 1=Yes)

  -  `H5_PRB` Problem sub: oth opiates/analg (0=No, 1=Yes)

  -  `H6_PRB` Problem sub: barbituates (0=No, 1=Yes)

  -  `H7_PRB` Problem sub: sedat/hyp/tranq (0=No, 1=Yes)

  -  `H8_PRB` Problem sub: cocaine (0=No, 1=Yes)

  -  `H9_PRB` Problem sub: amphetamines (0=No, 1=Yes)

  -  `H10_PRB` Problem sub: marijuana, cannabis (0=No, 1=Yes)

  -  `H11_PRB` Problem sub: hallucinogens (0=No, 1=Yes)

  -  `H12_PRB` Problem sub: inhalants (0=No, 1=Yes)

  -  `POLYSUB` Polysubstance abuser y/n (0=No, 1=Yes)

  -  `SMOKER` Current smoker (every/some days) y/n (0=No, 1=Yes)

  -  `O1B_REC` Family/friends heavy drinkers y/n (0=No, 1=Yes)

  -  `O1C_REC` Family/friends use drugs y/n (0=No, 1=Yes)

  -  `O1D_REC` Family/fiends support abst. y/n (0=No, 1=Yes)

  -  `O2_REC` Live-in partner drinks/drugs y/n (0=No, 1=Yes)

  -  `PHYABUSE` Physical abuse-stranger or family (0=No, 1=Yes)

  -  `SEXABUSE` Sexual abuse-stranger or family (0=No, 1=Yes)

  -  `PHSXABUS` Any abuse (0=No, 1=Yes)

  -  `ABUSE2` Type of abuse (0=No abuse, 1=Physical only, 2=Sexual only,
     3=Physical and sexual)

  -  `ABUSE3` Type of abuse (0=No abuse, 1=Physical only, 2=Sexual +/-
     physical (0=No, 1=Yes)

  -  `CURPHYAB` Current abuse-physical (0=No, 1=Yes)

  -  `CURSEXAB` Current abuse-sexual (0=No, 1=Yes)

  -  `CURPHYSEXAB` Curent abuse-physical or sexual (0=No abuse,
     1=Physical only, 2=Sexual +/- physical)

  -  `FAMABUSE` Family abuse-physical or sexual (0=No, 1=Yes)

  -  `STRABUSE` Stranger abuse-physical or sexual (0=No, 1=Yes)

  -  `ABUSE` Abuse-physical or sexual (0=No abuse, 1= Family abuse, 2=
     Stranger only abuse)

  -  `RAWPF` Raw SF-36 physical functioning

  -  `PF` SF-36 physical functioning (0-100)

  -  `RAWRP` Raw SF-36 role-physical

  -  `RP` SF-36 role physical (0-100)

  -  `RAWBP` Raw SF-36 pain index

  -  `BP` SF-36 pain index (0-100)

  -  `RAWGH` Raw SF-36 general health perceptions

  -  `GH` SF-36 general health perceptions (0-100)

  -  `RAWVT` Raw SF-36 vitality

  -  `VT` SF-36 vitality 0-100)

  -  `RAWSF` Raw SF-36 social functioning

  -  `SF` SF-36 social functioning (0-100)

  -  `RAWRE` Raw SF-36 role-emotional

  -  `RE` SF-36 role-emotional (0-100)

  -  `RAWMH` Raw SF-36 mental health index

  -  `MH` SF-36 mental health index (0-100)

  -  `HT` Raw SF-36 health transition item

  -  `PCS` Standardized physical component scale-00

  -  `MCS` Standardized mental component scale-00

  -  `CES_D` CES-D score, measure of depressive symptoms, high scores
     are worse

  -  `CESD_CUT` CES-D score > 21 y/n (0=No, 1=Yes)

  -  `C_MS` ASI-Composite medical status

  -  `C_AU` ASI-Composite score for alcohol use

  -  `C_DU` ASI-Composite score for drug use

  -  `CUAD_C` CUAD-Cocaine

  -  `CUAD_H` CUAD-Heroin

  -  `RAW_RE` SOCRATES-Rocognition-Raw

  -  `DEC_RE` SOCRATES-Recognition-Decile

  -  `RAW_AM` SOCRATES-Ambivalence-Raw

  -  `DEC_AM` SOCRATES-Ambivalence-Decile

  -  `RAW_TS` SOCRATES-Taking steps-Raw

  -  `DEC_TS` SOCRATES-Taking steps-Decile

  -  `RAW_ADS` ADS score

  -  `PHYS` InDUC-2L-Physical-Raw

  -  `PHYS2` InDUC-2L-Physical 9Raw (w/o M48)

  -  `INTER` InDUC-2L-Interpersonal-Raw

  -  `INTRA` InDUC-2L-Intrapersonal-Raw

  -  `IMPUL` InDUL-2L-Impulse control-Raw

  -  `IMPUL2` InDUC-2L-Impulse control-Raw (w/0 M23)

  -  `SR` InDUC-2L-Social responsibility-Raw

  -  `CNTRL` InDUC-2L-Control score

  -  `INDTOT` InDUC-2LTotal drlnC sore-Raw

  -  `INDTOT2` InDUC-2L-Total drlnC-Raw- w/o M23 and M48

  -  `PSS_FR` Perceived social support-friends

  -  `PSS_FA` Perceived social support-family

  -  `DRUGRISK` RAB-Drug risk total

  -  `SEXRISK` RAB-Sex risk total

  -  `TOTALRAB` RAB-Total RAB sore

  -  `RABSCALE` RAB scale sore

  -  `CHR_6M` Chronic medical conds/HIV-past 6m y/n (0=No, 1=Yes)

  -  `RCT_LINK` Did subject link to primary care (RCT)–This time point
     (0=No, 1=Yes)

  -  `REG_MD` Did subject report having regular doctor–This time point
     (0=No, 1=Yes)

  -  `ANY_VIS` # visits to regular doctor's office–This time point

  -  `ANY_VIS_CUMUL` Cumulative # visits to regular doctor's office

  -  `PC_REC` Primary care received: Linked & #visits (0=Not linked,
     1=Linked, 1 visit, 2=Linked, 2+ visits)

  -  `PC_REC7` Primary cared received: linked & # visits (0=Not linked,
     1=Linked, 1 visit, 2=Linked, 2 visits, 3=Linked, 3 visits, 4=Linked,
     4 visits, 5= Linked, 5 visits, 6=Linked, 6+visits)

  -  `SATREAT` Any BSAS substance abuse this time point (0=No, 1=Yes)

  -  `DRINKSTATUS` Drank alcohol since leaving detox-6m

  -  `DAYSDRINK` Time (days) from baseline to first drink since leaving
     detox-6m

  -  `ANYSUBSTATUS` Used alcohol, heroin, or cocaine since leaving
     detox-6m

  -  `DAYSANYSUB` time (days) from baseline to first alcohol, heroin, or
     cocaine since leaving detox-6m

  -  `LINKSTATUS` Linked to primary care within 12 months (by
     administrative record)

  -  `DAYSLINK` Time (days) to linkage to primary care within 12 months
     (by administrative record)

  http://www.math.smith.edu/help

  Args:

    path: str.
      Path to directory which either stores file or otherwise file will
      be downloaded and extracted there.
      Filename is `help_full.csv`.
  Returns:

    Tuple of np.ndarray `x_train` with 1472 rows and 788 columns and
    dictionary `metadata` of column headers (feature names).
  """
  import pandas as pd
  path = os.path.expanduser(path)
  filename = 'help_full.csv'
  if not os.path.exists(os.path.join(path, filename)):
    url = 'https://raw.github.com/vincentarelbundock/Rdatasets/master/csv' \
          '/mosaicData/HELPfull.csv'
    maybe_download_and_extract(path, url,
                               save_file_name='help_full.csv',
                               resume=False)

  data = pd.read_csv(os.path.join(path, filename), index_col=0)
  x_train = data.values
  metadata = {'columns': data.columns}
  return x_train, metadata
