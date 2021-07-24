DROP TABLE IF EXISTS public.imdb_title_crew;

CREATE TABLE public.imdb_title_crew
(
    tconst varchar,
    "directors" varchar,
    "writers" varchar,
    PRIMARY KEY (tconst)
);

ALTER TABLE public.imdb_title_crew
    OWNER to postgres;