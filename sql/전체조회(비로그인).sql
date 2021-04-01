		SELECT 
        
        ingredient.ingredient_id,
        ingredient.ingredient_name,
        ingredient.ingredient_category,
        ingredient_avg.ingredient_avg_id,
        ingredient_avg.ingredient_avg_price,
        ingredient_avg.ingredient_avg_date,
        ingredient_avg.ingredient_avg_predict_price,
        count(watch.ingredient_id) AS 'watch'
        
        FROM ingredient, ingredient_avg, watch

        WHERE ingredient.ingredient_id = ingredient_avg.ingredient_id AND
        watch.ingredient_id = ingredient.ingredient_id AND
        ingredient_avg.ingredient_avg_date = "2019-01-01" AND
        watch.watch_date = "2019-01-01"
        
        GROUP BY watch.ingredient_id
        
        ORDER BY count(watch.ingredient_id) DESC;
        