package com.ssafy.j301.mapper;

import java.util.List;
import org.springframework.stereotype.Repository;
import com.ssafy.j301.ingredient.Ingredient;

@Repository
public interface IngredientMapper {

	public List<Ingredient> selectAll();

	public List<Ingredient> selectAllByLogin();

	public Ingredient selectByIngredientId(Long ingredientId);

	public Ingredient selectByIngredientName(String ingredientName);
}
