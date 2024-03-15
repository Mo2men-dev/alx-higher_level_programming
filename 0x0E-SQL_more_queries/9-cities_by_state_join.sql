-- lists all cities contained in the database
SELECT cities.`id`, cities.`name`, states.`name`
FROM `cities` INNER JOIN `states` ON cities.`state_id` = state.`id`
ORDER BY cities.`id`;
