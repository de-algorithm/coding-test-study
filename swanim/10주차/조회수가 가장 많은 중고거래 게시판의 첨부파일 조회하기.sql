SELECT concat("/home/grep/src/", board_id, '/', file_id, file_name, file_ext) as FILE_PATH
from (select b.file_id, b.file_ext, b.file_name, b.board_id, rank () over(order by views desc) as ranking
     from used_goods_board a
     inner join used_goods_file b on a.board_id = b.board_id
     ) as tb
where ranking = 1
order by file_id desc