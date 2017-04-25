use zetadev;
select * from reviewcomment_action;
select * from review;
select * from review_material;
select id,material_id,action_taken,position,approved,created_on from review_comment;

select * from review_tickets;
select * from review_authors;
select * from review_moderators;
select * from review_participants order by reviewid;
select * from review_participants order by participantid;
select * from review_commentors;
select * from review_conversations;
