package com.ssafy.j301.mapper;

import java.util.List;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Repository;
import com.ssafy.j301.popularity.Popularity;

@Repository
public interface PopularityMapper {

	@Cacheable(value = "selectPopularity")
	public List<Popularity> selectPopularity();
}
