.mode column
.headers ON
.separator ROW "\n"
.nullvalue NULL

-- use commands
--> sqlite3 taverner.db
--> .read taverner.sql
-- to load all sqlite data into database

.read colour/colour_create.sql
.read colour/colour_fill.sql
.read colour/colour_view.sql

.read element_type/element_type_create.sql
.read element_type/element_type_fill.sql
.read element_type/element_type_view.sql

.read element/element_create.sql
.read element/element_fill.sql
.read element/element_view.sql

.read effectiveness_type/effectiveness_type_create.sql
.read effectiveness_type/effectiveness_type_fill.sql
.read effectiveness_type/effectiveness_type_view.sql

.read element_effectiveness/element_effectiveness_create.sql
.read element_effectiveness/element_effectiveness_fill.sql
.read element_effectiveness/element_effectiveness_view.sql

.read move/move_create.sql
.read move/move_fill.sql
.read move/move_view.sql

.read name/name_create.sql
.read name/name_fill.sql
.read name/name_view.sql

.read species/species_create.sql
.read species/species_fill.sql
.read species/species_view.sql

.read item/item_create.sql
.read item/item_fill.sql
.read item/item_view.sql

.read food/food_create.sql
.read food/food_fill.sql
.read food/food_view.sql

.read char_type/char_type_create.sql
.read char_type/char_type_fill.sql
.read char_type/char_type_view.sql
