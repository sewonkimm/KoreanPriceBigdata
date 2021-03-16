package com.ssafy.j301.member;

import org.springframework.stereotype.Service;
import com.ssafy.j301.common.exception.ValidationException;
import com.ssafy.j301.common.security.Sha256;
import com.ssafy.j301.mapper.MemberMapper;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class MemberService {
	
	private final MemberMapper memberMapper;
	private final Sha256 sha256;
	
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
	
}
