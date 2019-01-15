CREATE TABLE statebioguides(
    bioguide VARCHAR(24),
    letter CHAR,
    lastname VARCHAR(60),
    firstname VARCHAR(60),
    district VARCHAR(100),
    date_added TIMESTAMP NOT NULL DEFAULT NOW()
);