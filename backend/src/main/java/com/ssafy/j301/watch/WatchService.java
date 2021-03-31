package com.ssafy.j301.watch;

import org.springframework.stereotype.Service;
import com.ssafy.j301.mapper.WatchMapper;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class WatchService {

	private final WatchMapper watchMapper;

	public Watch insertWatch(Watch watch) {
		watchMapper.insertWatch(watch);
		return watch;
	}

	public int selectCount(Long ingredientId) {
		return watchMapper.selectCount(ingredientId);
	}
}
