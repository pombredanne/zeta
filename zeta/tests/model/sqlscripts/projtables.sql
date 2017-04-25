use zetadev;

select * from projectteam_type order by id;

select * from project order by id;
select id,project_id from project_info order by project_id;
select * from mailinglist order by id;
select * from ircchannel order by id;
select id,project_id,componentname,comp_number from component order by id;
select id,project_id,milestone_name,mstn_number,completed,cancelled,due_date from milestone order by id;
select id,project_id,version_name,ver_number from version order by id;
select * from project_admins;
select * from project_licenses;
select * from project_logos;
select * from project_icons;
select * from project_tags;
select * from project_attachments;
select * from component_owners;
select * from component_tags;
select * from milestone_tags;
select * from version_tags;

select * from project_perm;
select * from projectgroup_perm;
select * from project_team order by project_id;
select * from project_team order by user_id;
