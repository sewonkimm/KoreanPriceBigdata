package com.ssafy.j301.ingredient;

import com.ssafy.j301.ingredientAvg.IngredientAvg;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class Ingredient {

	private Long ingredientId;

	private String ingredientName;

	private String ingredientNameCode;

	private String ingredientDetailName;

	private String ingredientDetailNameCode;

	private String ingredientCategory;

	private IngredientAvg ingredientAvg;
}
