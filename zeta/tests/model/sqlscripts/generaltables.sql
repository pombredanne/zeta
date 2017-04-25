use zetadev;
select * from system;
select * from tag order by id;
select * from attachment order by id;
select * from attachment_tags order by attachmentid;
select * from attachment_uploaders;
select id,licensename,summary,source from license order by id;
select * from license_attachments order by licenseid;
select * from license_tags order by licenseid;
