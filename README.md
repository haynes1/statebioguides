# statebioguides
Creation and maintenance of ids for every state legislator in America.

The StateBioguides class contains the methods necessary for:

- importing existing state legislator's bioguide ids from existingbioguides.csv
- updating the existing bioguides csv when new state legislators are added
- retrieving a list of all existing legislators
- generating an id
- retrieving an id
- checking an id based on other information such as: name, district, time


This system stores bioguide ids in two places, the csv file contained in this project, and a psql database defined in schema.sql




System Info

- Will be similar to bioguide ids for federal legislators
- - Ex. Federal bioguide A000009	
- - Will add the state abbreviatio + SL as a prefix to denote state legislature
- Example: NYSLA000001
- Guaranteeing Uniqueness:
- - The SLBID table contains 5 pieces of identifying information:
- - - state
- - - last name
- - - first name
- - - current or last held district number
- - - created at timestamp

