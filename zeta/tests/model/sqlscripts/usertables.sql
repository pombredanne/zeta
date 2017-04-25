use zetadev;
select * from permission_name order by id;
select * from permission_group order by id;
select * from permission_maps order by groupid;

select * from userrelation_type order by userid;

select * from user order by id;
select * from user_info order by user_id;
select * from user_permissions;
select * from user_photos order by userid;
select * from user_icons order by userid;

select * from user_relation order by userfrom_id;
select * from user_relation order by userto_id;
