		SELECT 
        
        ingredient.ingredient_id,
        ingredient.ingredient_name,
        ingredient.ingredient_category,
        ingredient_avg.ingredient_avg_id,
        ingredient_avg.ingredient_avg_price,
        ingredient_avg.ingredient_avg_date,
        ingredient_avg.ingredient_avg_predict_price,
        count(*) as 'watch'
        
        FROM ingredient, ingredient_avg, watch

        WHERE ingredient.ingredient_id = ingredient_avg.ingredient_id and
        watch.ingredient_id = ingredient.ingredient_id and
        ingredient_avg.ingredient_avg_date = "2019-01-01" and
        watch.watch_date = "2019-01-01"
        
        group by watch.ingredient_id
        
        order by 'watch';