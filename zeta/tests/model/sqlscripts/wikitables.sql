use zetadev;
select * from wiki_type order by id;
select * from wiki order by id;
select * from wikitable_map order by id;
select id,wiki_id,author_id,version_id,created_on from wiki_comment order by id;

select * from wiki_tags order by wikiid;
select * from wiki_attachments order by wikiid;
select * from wiki_projects order by wikiid;
select * from wiki_projects order by projectid;
