CREATE TABLE public.enumerator_partitioned (
    id SERIAL,
    supervisor_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    phone INTEGER NOT NULL,
    PRIMARY KEY (supervisor_id, id)
) PARTITION BY RANGE (supervisor_id);