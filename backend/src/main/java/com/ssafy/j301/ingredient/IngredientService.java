package com.ssafy.j301.ingredient;

import java.util.List;
import org.springframework.stereotype.Service;
import com.ssafy.j301.mapper.IngredientMapper;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class IngredientService {

	private final IngredientMapper ingredientMapper;

	public List<Ingredient> selectAll() {
		return ingredientMapper.selectAll();
	}

	public List<Ingredient> selectAllByLogin() {
		return ingredientMapper.selectAllByLogin();
	}

	public Ingredient selectByingredientId(Long ingredientId) {
		return ingredientMapper.selectByIngredientId(ingredientId);
	}

	public Ingredient selectByIngredientName(String ingredientName) {
		return ingredientMapper.selectByIngredientName(ingredientName);
	}
}
