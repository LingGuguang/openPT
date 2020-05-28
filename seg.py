



def seg(context, seg_type='jieba'):
    return seg_types[seg_type](context)

def seg_jieba(context):
    import jieba
    return jieba.cut(context)

def seg_thulac(context):
    from thulac import thulac as tlac
    lac = tlac(seg_only=True)
    return lac.cut(context, text=True)

def seg_baidulac(context):
    from LAC import LAC
    lac = LAC(mode='seg')
    return lac.run(context)


seg_types = {
    'jieba': seg_jieba,
    'thulac': seg_thulac,
    'baidulac': seg_baidulac
}


if __name__ == "__main__":
    text = "今天的街道好安静啊"
    print(seg(text, seg_type='baidulac'))