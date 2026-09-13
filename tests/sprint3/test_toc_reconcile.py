import sys
sys.path.insert(0,'scripts')
from toc_reconcile import detect_chapter_starts

pages=['目录\n第一章｜市场背景\n第二章｜任务与客户','摘要','摘要','第一章｜市场背景','第二章｜任务与客户','第三章｜竞争方案','第四章｜商业证据','第五章｜风险与边界','附录','资料来源 第一章｜市场背景']
starts,valid,hits=detect_chapter_starts(pages)
assert valid and starts=={'chapter-1':4,'chapter-2':5,'chapter-3':6,'chapter-4':7,'chapter-5':8}
_,duplicate_valid,_=detect_chapter_starts(pages[:4]+['第一章｜市场背景']+pages[4:])
assert not duplicate_valid
_,same_page_valid,_=detect_chapter_starts(['第一章｜市场背景\n第二章｜任务与客户','第三章｜竞争方案','第四章｜商业证据','第五章｜风险与边界'])
assert not same_page_valid
print('TOC FALSE-POSITIVE TESTS = PASS')
