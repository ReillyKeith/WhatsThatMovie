DROP TABLE IF EXISTS public.imdb_title_basic;

CREATE TABLE public.imdb_title_basic
(
    tconst varchar,
    "titleType" varchar,
    "primaryTitle" varchar,
    "originalTitle" varchar,
    "isAdult" varchar,
    "startYear" varchar,
    "endYear" varchar,
    "runtimeMinutes" varchar,
    "genres" varchar,
    PRIMARY KEY (tconst)
);

ALTER TABLE public.imdb_title_basic
    OWNER to postgres;