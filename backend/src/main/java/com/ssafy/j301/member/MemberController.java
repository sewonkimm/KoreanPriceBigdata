package com.ssafy.j301.member;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.RequiredArgsConstructor;

@Api(tags = "Members", description = "사용자  API")
@RequiredArgsConstructor
@RestController
@RequestMapping(value = "/members")
public class MemberController {
	
	private final MemberService memberService;
	
	@ApiOperation(value = "가입하기", notes = "중복 이메일, 이름을 검사합니다.")
    @PostMapping("/signup")
    public Member signup(@RequestBody Member member) {

        memberService.validateSignUp(member);
        return memberService.signup(member);
    }

}
