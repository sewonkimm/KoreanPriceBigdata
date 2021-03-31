package com.ssafy.j301.mapper;

import java.util.List;
import org.springframework.stereotype.Repository;
import com.ssafy.j301.favorite.Favorite;

@Repository
public interface FavoriteMapper {

	public void insertFavorite(Favorite favorite);

	public void deleteFavorite(Favorite favorite);

	public Favorite selectFavorite(Favorite favorite);

	public List<Favorite> selectAll(Long memberId);
}
