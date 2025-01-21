CREATE TABLE public.enumerator_partition_1
PARTITION OF public.enumerator_partitioned
FOR VALUES FROM (1) TO (11);

CREATE TABLE public.enumerator_partition_2
PARTITION OF public.enumerator_partitioned
FOR VALUES FROM (11) TO (21);

CREATE TABLE public.enumerator_partition_3
PARTITION OF public.enumerator_partitioned
FOR VALUES FROM (21) TO (31);