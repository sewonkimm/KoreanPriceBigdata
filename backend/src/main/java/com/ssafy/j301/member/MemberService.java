package com.ssafy.j301.member;

import java.util.HashMap;
import java.util.Map;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import com.ssafy.j301.common.exception.LoginFailedException;
import com.ssafy.j301.common.exception.ValidationException;
import com.ssafy.j301.common.security.Sha256;
import com.ssafy.j301.mapper.MemberMapper;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class MemberService {

	private final MemberMapper memberMapper;
	private final Sha256 sha256;
	private final JwtService jwtService;

	public Member signup(Member member) {
		member.setMemberPassword(sha256.encryption(member.getMemberPassword()));
		memberMapper.insertMember(member);
		return member;
	}

	public void validateSignUp(final Member member) {

		if (memberMapper.checkEmail(member.getMemberEmail())) {
			throw new ValidationException("이미 존재하는 이메일입니다.");
		}
	}

	public ResponseEntity<Map<String, Object>> login(Member member) {

		Map<String, Object> resultMap = new HashMap<String, Object>();
		String password = sha256.encryption(member.getMemberPassword());
		member.setMemberPassword(password);

		int matchMember = memberMapper.getMemberByMemberEmailAndPassword(member);

		if (matchMember != 1) {
			throw new LoginFailedException("샤용자가 존재하지 않거나 비밀번호가 틀렸습니다.");
		}

		member.setMemberPassword(member.getMemberPassword());

		String token = jwtService.create(member);
		resultMap.put("accesstoken", token);
		resultMap.put("message", "Success");
		return new ResponseEntity<Map<String, Object>>(resultMap, HttpStatus.ACCEPTED);

	}

}