BEGIN
  FOR cur_rec IN (SELECT table_name FROM user_tables WHERE table_name != 'user')
  LOOP
    EXECUTE IMMEDIATE ('DROP TABLE ' || cur_rec.table_name || ' CASCADE CONSTRAINTS');
  END LOOP;
  EXECUTE IMMEDIATE ('DROP TABLE "user" CASCADE CONSTRAINTS');
END;