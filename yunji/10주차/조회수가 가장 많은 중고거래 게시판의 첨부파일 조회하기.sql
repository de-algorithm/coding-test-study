-- 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회
-- 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬
SELECT CONCAT('/home/grep/src/',ugb.BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) FILE_PATH
FROM USED_GOODS_FILE ugf 
RIGHT JOIN
    (SELECT * FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
    ) ugb 
ON ugf.BOARD_ID = ugb.BOARD_ID
ORDER BY FILE_ID DESC