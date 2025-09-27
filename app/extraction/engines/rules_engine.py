import asyncio
from typing import List, Dict
from ..base import Extractor, ProgressCb

def naive_extract_dialogue_spans(text: str) -> List[Dict]:
    spans: List[Dict] = []
    n, i, in_q, start = len(text), 0, False, 0
    blocks: list[tuple[int,int,bool]] = []
    while i < n:
        if text[i] == '"':
            if in_q:
                blocks.append((start, i + 1, True)); in_q = False; start = i + 1
            else:
                if start < i: blocks.append((start, i, False))
                in_q = True; start = i
        i += 1
    if start < n: blocks.append((start, n, in_q))
    last = None
    for s, e, is_d in blocks:
        if e <= s: continue
        typ = "dialogue" if is_d else "narrator"
        if last and not is_d and last["type"] == "narrator" and last["span_end"] == s:
            last["span_end"] = e
        else:
            rec = {"span_start": s, "span_end": e, "type": typ}
            spans.append(rec); last = rec
    return spans

class RulesEngine(Extractor):
    name = "rules"
    async def extract_full(self, *, text: str, passes: int, max_char_buffer: int) -> List[Dict]:
        return await asyncio.to_thread(lambda: naive_extract_dialogue_spans(text))
    
    
    async def extract_chunked(self, *, text: str, buffer_chars: int, overlap_chars: int,
                              passes: int, resume_char_offset: int, on_progress: ProgressCb) -> List[Dict]:
        spans = await self.extract_full(text=text, passes=passes, max_char_buffer=buffer_chars)
        if on_progress: on_progress(len(text), len(text), passes, 0)
        return spans