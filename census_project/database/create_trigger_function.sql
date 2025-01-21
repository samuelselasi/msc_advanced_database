CREATE OR REPLACE FUNCTION log_user_activity()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.user_activity_log (table_name, operation_type, record_id)
    VALUES (TG_TABLE_NAME, TG_OP, NEW.id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;