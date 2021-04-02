package com.ssafy.j301.ingredientAvg;

import java.time.LocalDate;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@AllArgsConstructor
@NoArgsConstructor
public class IngredientAvg {

	private Long ingredientAvgId;

	private Long ingredientId;

	private LocalDate ingredientAvgDate;

	private int ingredientAvgPreviousPrice;

	private int ingredientAvgPrice;

	private int ingredientAvgPredictPrice;
	
}
