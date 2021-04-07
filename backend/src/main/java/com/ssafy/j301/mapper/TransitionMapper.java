package com.ssafy.j301.mapper;

import java.util.List;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Repository;
import com.ssafy.j301.transition.Transition;

@Repository
public interface TransitionMapper {

	@Cacheable(value = "selectTransition")
	public List<Transition> selectTransition(Long ingredientId);
}
