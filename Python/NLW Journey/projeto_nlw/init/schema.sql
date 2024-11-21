CREATE TABLE IF NOT EXISTS 'trips'(
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date DATETIME,
    end_date DATETIME,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER
);

CREATE TABLE IF NOT EXISTS 'emails_to_invite' (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    email TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);

CREATE TABLE IF NOT EXISTS 'links' (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    link TEXT NOT NULL,
    title TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES trips(id)
);


CREATE TABLE 'participants' (
	id TEXT PRIMARY KEY,
	trip_id TEXT NOT NULL,
	emails_to_invite_id TEXT NOT NULL,
	name TEXT NOT NULL,
	is_confirmed INTEGER,
	FOREIGN KEY (trip_id) REFERENCES trips(id)
	FOREIGN KEY (emails_to_invite_id) REFERENCES emails_to_invite(id)
);

CREATE TABLE 'activities' (
	id TEXT PRIMARY KEY,
	trip_id INTEGER,
	title TEXT NOT NULL,
	occurs_at DATETIME,
	FOREIGN KEY (trip_id) REFERENCES trips(id)
);