"use client";

import { Switch } from "../ui/switch";
import { Button } from "../ui/button";
import { Card } from "../ui/card";
import { Checkbox } from "../ui/checkbox";
import { Label } from "../ui/label";
import {
	Combobox,
	ComboboxContent,
	ComboboxEmpty,
	ComboboxInput,
	ComboboxItem,
	ComboboxList,
} from "@/components/ui/combobox";
import {
	Select,
	SelectContent,
	SelectGroup,
	SelectItem,
	SelectTrigger,
	SelectValue,
} from "@/components/ui/select";
import { Input } from "../ui/input";
import { Slider } from "../ui/slider";

export default function FilterPage() {
	const tags = [
		"Psychological",
		"Time Travel",
		"Tragedy",
		"Military",
		"Romance",
	];

	const genres = ["Action", "Drama", "Fantasy", "Sci-Fi", "Mystery"];

	const studios = ["MAPPA", "Madhouse", "Wit Studio", "Ufotable", "Bones"];

	return (
		<div className="h-screen overflow-hidden bg-[#0b1120]">
			<div className="h-full overflow-y-auto px-4 py-6 space-y-8 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent">
				<div>
					<h2 className="text-xl font-semibold text-white">Filters</h2>

					<Button className="mt-2 bg-purple-600 hover:bg-purple-500">
						Apply Filters
					</Button>

					<Button
						className="ml-2 border-slate-700 text-slate-200 hover:bg-slate-800"
						variant="outline"
					>
						Clear Filters
					</Button>

					<Card className="mt-4 bg-[#0f172a] border border-slate-800 text-slate-100 p-6 space-y-4">
						<div className="flex items-center gap-3">
							<Checkbox />
							<Label className="text-slate-300">Show sequels</Label>
						</div>

						<div className="flex items-center gap-3">
							<Checkbox />
							<Label className="text-slate-300">Experimental mode</Label>
						</div>

						<div className="flex items-center gap-3">
							<Checkbox />
							<Label className="text-slate-300">Show 18+ rated</Label>
						</div>
					</Card>

					<Card className="mt-6 bg-[#0f172a] border border-slate-800 text-slate-100 p-6 space-y-4">
						<div>
							<Select>
								<SelectTrigger className="w-[250px] bg-slate-900 border-slate-700 text-slate-100">
									<SelectValue placeholder="Tag Importance in recommendation" />
								</SelectTrigger>
								<SelectContent>
									<SelectGroup>
										<SelectItem value="low">Low</SelectItem>
										<SelectItem value="medium">Medium</SelectItem>
										<SelectItem value="high">High</SelectItem>
									</SelectGroup>
								</SelectContent>
							</Select>
						</div>

						<div>
							<Select>
								<SelectTrigger className="w-[250px] bg-slate-900 border-slate-700 text-slate-100">
									<SelectValue placeholder="Popularity influence" />
								</SelectTrigger>
								<SelectContent>
									<SelectGroup>
										<SelectItem value="negative">Boost Underrated</SelectItem>
										<SelectItem value="low">Low</SelectItem>
										<SelectItem value="medium">Medium</SelectItem>
										<SelectItem value="high">High</SelectItem>
									</SelectGroup>
								</SelectContent>
							</Select>
						</div>
					</Card>

					<Card className="mt-6 bg-[#0f172a] border border-slate-800 text-slate-100 p-6 space-y-6">
						<div>
							<Input
								type="number"
								placeholder="Minimum number of episodes (e.g. 12)"
								className="bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
							/>
							<Input
								type="number"
								placeholder="Maximum number of episodes (e.g. 100)"
								className="mt-3 bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
							/>
							<Button className="mt-2 bg-purple-600 hover:bg-purple-500">
								Apply Episode Count Filter
							</Button>
						</div>

						<div>
							<Input
								type="number"
								placeholder="Minimum release year (e.g. 2005)"
								className="bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
							/>
							<Input
								type="number"
								placeholder="Maximum release year (e.g. 2023)"
								className="mt-3 bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
							/>
							<Button className="mt-2 bg-purple-600 hover:bg-purple-500">
								Apply Release Year Filter
							</Button>
						</div>
					</Card>

					<Card className="mt-6 bg-[#0f172a] border border-slate-800 text-slate-100 p-6 space-y-6">
						<div>
							<Label className="mb-2 text-slate-300">
								Show items with mean score at least:
							</Label>
							<Slider
								defaultValue={[75]}
								max={100}
								step={1}
								className="w-full"
							/>
						</div>

						<div>
							<Combobox items={studios}>
								<ComboboxInput
									placeholder="Filter by studio (e.g. MAPPA)"
									className="bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
								/>
								<ComboboxContent>
									<ComboboxEmpty>No studio found.</ComboboxEmpty>
									<ComboboxList>
										{(item) => (
											<ComboboxItem key={item} value={item}>
												{item}
											</ComboboxItem>
										)}
									</ComboboxList>
								</ComboboxContent>
							</Combobox>
							<Button className="mt-2 bg-purple-600 hover:bg-purple-500">
								Add Studio
							</Button>
						</div>

						<div>
							<Switch className="w-10 h-5" />
							<Label className="ml-2 text-slate-300">
								Show or hide selected tags
							</Label>

							<Combobox items={tags}>
								<ComboboxInput
									placeholder="Filter by tag (e.g. Psychological)"
									className="mt-3 bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
								/>
								<ComboboxContent>
									<ComboboxEmpty>No tag found.</ComboboxEmpty>
									<ComboboxList>
										{(item) => (
											<ComboboxItem key={item} value={item}>
												{item}
											</ComboboxItem>
										)}
									</ComboboxList>
								</ComboboxContent>
							</Combobox>

							<Button className="mt-2 bg-purple-600 hover:bg-purple-500">
								Add Tag
							</Button>
						</div>

						<div>
							<Combobox items={genres}>
								<Switch className="w-10 h-5 mb-2" />
								<Label className="ml-2 text-slate-300">
									Show or hide selected genres
								</Label>

								<ComboboxInput
									placeholder="Filter by genre (e.g. Sci-Fi)"
									className="mt-3 bg-slate-900 border-slate-700 text-slate-100 placeholder:text-slate-500"
								/>
								<ComboboxContent>
									<ComboboxEmpty>No genre found.</ComboboxEmpty>
									<ComboboxList>
										{(item) => (
											<ComboboxItem key={item} value={item}>
												{item}
											</ComboboxItem>
										)}
									</ComboboxList>
								</ComboboxContent>
							</Combobox>

							<Button className="mt-2 bg-purple-600 hover:bg-purple-500">
								Add Genre
							</Button>
						</div>

						<div>
							<Select>
								<SelectTrigger className="w-[200px] bg-slate-900 border-slate-700 text-slate-100">
									<SelectValue placeholder="Select media type" />
								</SelectTrigger>
								<SelectContent>
									<SelectGroup>
										<SelectItem value="anime">Anime</SelectItem>
										<SelectItem value="manga">Manga</SelectItem>
									</SelectGroup>
								</SelectContent>
							</Select>
						</div>
					</Card>
				</div>
			</div>
		</div>
	);
}
