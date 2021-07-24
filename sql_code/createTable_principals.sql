DROP TABLE IF EXISTS public.imdb_title_principals;

CREATE TABLE public.imdb_title_principals
(
    tconst varchar,
    "ordering" varchar,
    "nconst" varchar,
    "category" varchar,
    "job" varchar,
    "characters" varchar,
    PRIMARY KEY (tconst)
);

ALTER TABLE public.imdb_title_principals
    OWNER to postgres;