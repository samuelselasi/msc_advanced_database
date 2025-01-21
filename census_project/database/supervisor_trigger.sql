CREATE TRIGGER supervisor_activity_log
AFTER INSERT OR UPDATE OR DELETE
ON public.supervisor
FOR EACH ROW
EXECUTE FUNCTION log_user_activity();