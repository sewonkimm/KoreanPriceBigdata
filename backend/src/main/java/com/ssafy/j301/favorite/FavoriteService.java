package com.ssafy.j301.favorite;

import java.util.List;
import org.springframework.stereotype.Service;
import com.ssafy.j301.mapper.FavoriteMapper;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class FavoriteService {

	private final FavoriteMapper favoriteMapper;

	public void insertFavorite(Favorite favorite) {
		Favorite checkFavorite = favoriteMapper.selectFavorite(favorite);
		if (checkFavorite == null) {
			favoriteMapper.insertFavorite(favorite);
		} else {
			favoriteMapper.deleteFavorite(favorite);
		}
	}

	public List<Favorite> selectAll(Long memberId) {
		return favoriteMapper.selectAll(memberId);
	}

	public Favorite selectFavorite(Favorite favorite) {
		return favoriteMapper.selectFavorite(favorite);
	}
}
