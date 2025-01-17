-- Left Join
SELECT
    enumerator.id AS enumerator_id,
    enumerator.name AS enumerator_name,
    enumerator.phone AS enumerator_phone,
        supervisor.name As supervisor_name,
        supervisor.phone As supervisor_phone
FROM
    public.enumerator enumerator
LEFT JOIN
    public.supervisor supervisor
ON
    enumerator.supervisor_id = supervisor.id;
