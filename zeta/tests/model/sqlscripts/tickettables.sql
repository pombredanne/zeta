use zetadev;
select * from ticket_status;
select * from ticket_type;
select * from ticket_severity;
select id,ticket_number,type_id,severity_id,created_on from ticket order by id;
select * from ticket_status_history;
select id,ticket_id,created_on from ticket_comment;
select * from ticket_reference;

select * from ticket_projects;
select * from ticket_promptusers;
select * from ticket_components;
select * from ticket_milestones;
select * from ticket_versions;
select * from ticket_blockers order by blockedbyid;
select * from ticket_blockers order by blockingid;
select * from ticket_hier order by partckid;
select * from ticket_hier order by childtckid;
select * from ticket_attachments;
select * from ticket_tags;
select * from ticketstatus_owners;
select * from ticketcomment_authors;
select * from ticket_conversations;
