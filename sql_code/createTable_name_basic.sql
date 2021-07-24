CREATE TABLE public.imdb_name_basic
(
    nconst varchar,
    "birthYear" int,
    "deathYear" int,
    "primaryName" varchar,
    "primaryProfession" varchar,
    "knownForTitles" varchar,
    PRIMARY KEY (nconst)
);

ALTER TABLE public.imdb_name_basic
    OWNER to postgres;