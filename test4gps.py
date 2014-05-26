import gps


session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

for report in session:
  print report
  


#with Crlt c should exit the session




