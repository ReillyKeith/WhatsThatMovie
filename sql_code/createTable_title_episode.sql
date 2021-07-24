DROP TABLE IF EXISTS public.imdb_title_episode;

CREATE TABLE public.imdb_title_episode
(
    tconst varchar,
    "parentTconst" varchar,
    "seasonNumber" varchar,
    "episodeNumber" varchar,
    PRIMARY KEY (tconst)
);

ALTER TABLE public.imdb_title_episode
    OWNER to postgres;