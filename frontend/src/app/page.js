"use client";
import LoginPage from "./loginPage/page";
import Recommendations from "./recommendations/page";

export default function Home() {
	return (
		<div>
			{localStorage.getItem("username") != null ? (
				<Recommendations />
			) : (
				<LoginPage />
			)}
		</div>
	);
}
