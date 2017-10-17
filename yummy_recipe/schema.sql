drop table if exists recipe_categorys;
create table recipe_categorys (
  id integer primary key autoincrement,
  recipe_category text not null,
  further_info text not null
);
drop table if exists recipes;
create table recipes (
  id integer primary key autoincrement,
  recipe text not null,
  steps text not null
);
