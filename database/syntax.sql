CREATE TABLE table_adjuster_valve_hla (
	id INTEGER PRIMARY KEY,
	name_line TEXT NOT NULL,
	name_part TEXT NOT NULL,
	quantity TEXT NOT NULL ,
	delay TEXT NOT NULL,
  status TEXT NOT NULL,
  andon TEXT NOT NULL,
  datetime DEFAULT (DATETIME('now', 'localtime'))
);
