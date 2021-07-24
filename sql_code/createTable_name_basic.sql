DROP TABLE IF EXISTS public.imdb_name_basic;

CREATE TABLE public.imdb_name_basic
(
    nconst varchar,
    "birthYear" varchar,
    "deathYear" varchar,
    "primaryName" varchar,
    "primaryProfession" varchar,
    "knownForTitles" varchar,
    PRIMARY KEY (nconst)
);

ALTER TABLE public.imdb_name_basic
    OWNER to postgres;