drop table if exists users;
create table users (
  id         integer primary key autoincrement,
  username   text not null,
  password   text not null,
  name       text not null
);
drop table if exists recipe_categorys;
create table recipe_categorys (
  recipe_category_id   integer primary key autoincrement,
  recipe_category text not null,
  further_info    text not null
);
drop table if exists recipes;
create table recipes (
  recipe_id                 integer primary key autoincrement,
  recipe text               not null,
  recipe_recipe_catedory_id integer,
  FOREIGN KEY(recipe_recipe_catedory_id) REFERENCES recipe_categorys(recipe_category_id)
);
