DROP TABLE IF EXISTS public.imdb_title_ratings;

CREATE TABLE public.imdb_title_ratings
(
    tconst varchar,
    "averageRating" varchar,
    "numVotes" varchar,
    PRIMARY KEY (tconst)
);

ALTER TABLE public.imdb_title_ratings
    OWNER to postgres;