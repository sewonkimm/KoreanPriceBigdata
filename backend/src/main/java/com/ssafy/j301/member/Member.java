package com.ssafy.j301.member;

import java.time.LocalDate;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.NonNull;
import lombok.Setter;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class Member {

	private Long memberId;

	@NonNull
	private String memberEmail;

	@NonNull
	private String memberName;

	@NonNull
	private String memberPassword;

	
	private LocalDate memberBirth;

	
	private char memberGender;

	
	private String memberArea;

}
