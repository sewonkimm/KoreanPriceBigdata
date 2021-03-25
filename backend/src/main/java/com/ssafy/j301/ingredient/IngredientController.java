package com.ssafy.j301.ingredient;

import java.util.List;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;

@Api(tags = "Ingredients", description = "농축산물 API")
@RestController
@RequiredArgsConstructor
@RequestMapping(value = "/ingredients")
public class IngredientController {

	private final IngredientService ingredientService;

	@ApiOperation(value = "농축산물 전체 조회", notes = "Ingredient를 리턴합니다.")
	@GetMapping("/")
	public List<Ingredient> selectAll() {
		return ingredientService.selectAll();
	}

	@ApiOperation(value = "농축산물 ID로 조회", notes = "IngredientId로 조회한 결과를 리턴합니다.")
	@GetMapping("/detail")
	public Ingredient selectByIngredientId(Long ingredientId) {
		return ingredientService.selectByingredientId(ingredientId);
	}
}
